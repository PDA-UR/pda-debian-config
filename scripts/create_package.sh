#!/bin/sh

####################################################
# This script generates Debian meta packages       #
# (e.g., packages which do not install any files   #
# but just define other packages to be installed). #
####################################################


DIR_TEMPLATE="./pda-package-template"
PACKAGE_NAME="${1}"
DEPENDENCIES=$(cat ${PACKAGE_NAME}.txt)

cp -r "${DIR_TEMPLATE}" "${PACKAGE_NAME}"

sed -i -e "s/PACKAGE_NAME/${PACKAGE_NAME}/g"  "${PACKAGE_NAME}/DEBIAN/control"
sed -i -e "s/DEPENDENCIES/${DEPENDENCIES}/g"  "${PACKAGE_NAME}/DEBIAN/control"

dpkg --build "${PACKAGE_NAME}"

