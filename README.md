# adaptive-thresholding
Create a PDF suitable for economic printing from photos

## Create a PDF suitable for economic printing from photos

A little script that performs adaptive threshold in photos.

With the advent of Coronavirus and the remote learning spike a lot of
children and professors started exchange learning material via electronic
means.

Normally this is done via phones where applications like CamScanner perform
adaptive thresholding.  Adaptive thresholding is a must if you need to save
some ink in order to print another day.  Adaptive thresholding is not only
environmentally friendy but helps your strained eyes by increasing the
contrast of the generated image and lowers your bandwidth cap by producing
images with much smaller size.

However many people are not aware of the adaptive threshold and the
specialized scanner application and so they send images captured by
the phone's camera (photos). These have the following problems in
case you didn't read the previous paragraph.

1. They have large grays areas and degradation
2. They have small contrast (variation of gray) and shadows
3. They have much bigger size typically 1 to 7 ratio
4. Since they are bigger it takes more time to upload, download and more
space on disk

The problem though is that on Linux there is no easy to perform the
adaptive thresholding. Gimp doesn't do it.

## Solution

The followng python script employs opencv and its python bindings
to perform adapative thresholding in all images in a directory
(not recursively) and launches the default PDF viewer with the
assembled PDF.

A desktop file is also provided if you want to have right click integration
in your file manager for this kind of operations.

## Dependencies

* python3
* python3-opencv
* xdg-utils
* imagemagick
* A default PDF viewer that is associated with xdg-open


In a normal desktop

```
apt install python3-opencv
```

is all you need.

## Installation

Put or link th create-adaptive-threshold-pdf.py file in /usr/local/bin

```
$sudo su -
#cp create-adaptive-threshold-pdf.py /usr/local/bin/
```

### For KDE

Run this to locate where are the ServiceMenu folder (user and system)

```
kf5-config --path services
```

Put the create-adaptive-threshold-pdf.desktop in one of them

```
$sudo su -
#cp create-adaptive-threshold-pdf.desktop /usr/share/kservices5/ServiceMenus/
```

Close all dolphin instances and run kbuildsycoca5

```
kbuildsycoca5
```

1. Run dolphin again
1. Locate a directory that has the scanned imaged
1. Righ click / Actions / Create PDF
1. Okular should start with all the images in the directory assembed in one tidy PDF
suitable for economic printing that doesn't make your eyes and your pocket
bleed.


## Pitfalls

You may see

```
convert-im6.q16: attempt to perform an operation not allowed by the security policy `PDF' @ error/constitute.c/IsCoderAuthorized/421.
```

Here is the answer: https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion
