from PIL import Image
import argparse
import os.path
import logging


def get_args():
    usage = "image_resize.py [-h] [-W WIDTH] [-H HEIGHT] or " \
            "[-S SCALE] [-o OUTPUT_PATH] image_path"
    parser = argparse.ArgumentParser(description="Image resizer script\n", usage=usage)
    parser.add_argument("image_path", help="path to open resizing image", type=str)
    parser.add_argument("-W", "--width", type=int, default=0)
    parser.add_argument("-H", "--height", type=int, default=0)
    parser.add_argument("-S", "--scale", type=float, default=0)
    parser.add_argument("-o", "--output", dest="output_path", type=str,
                        help="path to output resized image")
    parser.conflict_handler = check_args_validation(parser)
    return parser.parse_args()


def check_args_validation(parser):
    args = parser.parse_args()
    scale, width, height = args.scale, args.width, args.height
    if (width or height) and scale:
        raise parser.error("Args combinations can only be "
                           "width, height, width and height or scale.\n")
    if not width and not height and not scale:
        raise parser.error("Specify resize args. Args combinations can only be "
                           "width, height, width and height or scale.\n")
    if args.image_path and not os.path.exists(args.image_path):
        raise argparse.ArgumentTypeError("path {} does not exist".format(args.image_path))
    if args.output_path and not os.path.exists(args.output_path):
        raise argparse.ArgumentTypeError("path {} does not exist".format(args.output_path))


def get_new_width_and_height(new_height, new_width, origin_width, origin_height):
    if new_width and not new_height:
        scale = new_width / origin_width
    if new_height and not new_width:
        scale = new_height / origin_height
    return int(origin_width * scale), int(origin_height * scale)


def check_propotions_matching(origin_width, origin_height, new_width, new_height):
    permissible_error = 0.005
    scale_difference = abs(new_width / origin_width - new_height / origin_height)
    if scale_difference > permissible_error:
        logging.warning("Proportions does not match the original image")


def save_resized_image(new_width, new_height, origin_filepath, output_filepath):
    image_name, image_extension = os.path.splitext(os.path.basename(origin_filepath))
    template = "%s__%dx%d%s"
    resized_image_name = template % (image_name, new_width, new_height, image_extension)
    if output_filepath:
        resized_image_path = os.path.join(output_filepath, resized_image_name)
        resized_image.save(resized_image_path)
        logging.info(u"Image was successfully saved to saving directory")
        return
    else:
        resized_image.save(resized_image_name)
        logging.info(u"Image was successfully saved to script directory")


if __name__ == "__main__":
    args = get_args()
    logging.basicConfig(level=logging.INFO)
    image = Image.open(args.image_path)
    width, height = image.width, image.height
    if args.scale:
        new_width, new_height = int(args.scale * width), int(args.scale * height)
    if (args.width and not args.height) or (args.height and not args.width):
        new_width, new_height = get_new_width_and_height(args.width, args.height,
                                                         width, height)
    if args.width and args.height:
        new_width, new_height = int(args.width), int(args.height)
        check_propotions_matching(width, height, new_width, new_height)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    save_resized_image(new_width, new_height, args.image_path, args.output_path)
    image.close()
    resized_image.close()
