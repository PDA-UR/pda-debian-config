
all: pda-packages-base.deb pda-packages-gui.deb pda-packages-development.deb pda-packages-multimedia.deb pda-packages-hardware.deb pda-packages-fonts.deb pda-packages-misc.deb pda-packages-network.deb pda-packages-python.deb pda-packages-special.deb pda-packages-tex.deb pda-packages-r.deb pda-packages-unsorted.deb 

clean:
	-rm -r pda-packages-*

%.deb: %.txt
	./scripts/create_package.sh $*

%.txt: ./source/pda-packages.txt
	./scripts/split_package_list.py $<
	
