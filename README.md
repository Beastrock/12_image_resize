# Image Resizer  

Script resizes image and outputs a new one with desired resolution. It is based on [Pillow](https://pillow.readthedocs.io) and works with jpg and png images.

## Getting Started

`git clone https://github.com/Beastrock/12_image_resize.git`  
`pip install -r requirements.txt` 

## Usage
`python image_resize.py [-h] [-W WIDTH] [-H HEIGHT] or [-S SCALE] [-o OUTPUT_PATH] image_path`

###Arguments

ARG NAME | TYPE| USAGE | DESCRIPTION
--- | --- | --- | ---|
**Scale** | float | `-S, --scale`| resizing scale (0 > scale < 1 and  scale > 1)
**Width** | int | `-W, --width`| width of new image
**Height** | int | `-H, --height`| height of new image
**Output** | string | `-o, --output`| path to output resized image
**Help** | string | `-h, --help`| show help message  

### Working logic
- Arguments combinations can only be width, height, width and height or scale. You can't use scale and width or height.    
- If you specify only width or height, second size parameter will be calculated by the same scale to save image proportions.
- If you specify width and height, script will check proportions matching and will print message if they do not match.
- Resized image name template: `<original_image_name>__<new_width>x<new)height>.<image_extension>`.
- If output path is not specified, resized image will be put at the script folder. 

###Examples

```
python image_resize.py D:\img.jpg  -H 1000 -W 1500   
result: img__1500x1000.jpg saved in script folder  

python image_resize.py D:\img.jpg -S 0.5 -o D:\img_foder  
result: img__1500x1000.jpg saved in D:\img_foder   
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

