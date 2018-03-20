# pda-debian-config - some useful Debian packages 

This repo contains a few small Debian metapackages (i.e., packages that do not contain any files but only define other packages that should be installed).
The scripts and raw lists for generating the packages are also included.

##Installing a package

``apt install ./packages/pda-packages-base.deb`` 

(the leading ``./`` is necessary for ``apt`` to recognize this as a local path).


## Contents of the packages:

(the letter in the first column is used for tagging the package in ``source/pda-packages.txt``)

| L | suffix       | description                                               |
|---|--------------|-----------------------------------------------------------|
| B | base         | basic CLI tools                                           |
| G | gui          | basic GUI tools                                           |
| M | multimedia   | photo/video/audio tools                                   |
| N | network      | networking tools                                          |
| D | development  | development tools                                         |
| P | python       | python tools and libraries                                |
| R | r            | R tools and libraries                                     |
| T | tex          | LaTeX stuff                                               |
| F | fonts        | fonts                                                     |
| H | hardware     | tools for embedded development (microcontrollers, etc)    |
| S | special      | specialized tools for various needs (do not install)      |
| ? | unsorted     | stuff where I don't know what it is                       |
| # | ugly         | stuff that is not installable                             |




Additional interesting tools that are not included in Debian:

* [Arduino IDE](https://arduino.cc)
* [Baudline](http://www.baudline.com/) - signal analyzer
* [GitKraken](https://www.gitkraken.com/) - cross-platform Git GUI (commercial pro version)
* [Master PDF Editor](https://code-industry.net/masterpdfeditor/) - cross-platform PDF editor (commercial)
* [Seafile](https://www.seafile.com/en/home/)
* [ViewGlob](https://github.com/sjbach/viewglob) 
