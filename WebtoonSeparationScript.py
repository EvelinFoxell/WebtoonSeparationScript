#!/bin/bash
from PIL import Image # PIL is from Pillow
import sys, os

usage = 'Run script with the path to the file. Example: python WebtoonSeparationScript.py ./myImage.png'

left = 0
imagewidth = 800
imageheigth = 1280

path = sys.argv[1]

def loadImage(imagePath):
	try:
		originalImage = Image.open(imagePath)
		return originalImage
	except Exception as e:
		print('Could not load image: ' + "{0}".format(e) + ' ' + usage)

def createFolder(folderName):
	try:
		os.mkdir(folderName)
	except FileExistsError:
		print('Could not create directory; it already exists.')

def cutImage(originalImage):
	imageName = path.split('/')[-1].split('.')[0]
	resultDirectory = 'croppedImages_' + imageName
	width, imageLength = originalImage.size
	keepCropping = True
	top = 0
	bottom = imageheigth
	imageNumber = 1
	print('Creating directory ' + resultDirectory)
	createFolder(resultDirectory)
	while keepCropping:
		print('Cropping page ' + str(imageNumber))
		cropped = originalImage.crop((left, top, imagewidth, bottom))
		cropped.save('./' + resultDirectory + '/' + str(imageNumber) + '.png', 'PNG')
		if(imageLength > bottom):
			newHeight = bottom + imageheigth
			bottom = newHeight if newHeight < imageLength else imageLength 
			top += imageheigth
			imageNumber += 1
		else: 
			keepCropping = False

print('Loading image...')
originalImage = loadImage(path)
cutImage(originalImage)
print('Cropping has been completed! Thank you, see you next time!')
