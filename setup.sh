#!/bin/bash

bldblu=${txtbld}$(tput setaf 4)


[ ! -e titilliumweb ] && mkdir -p titilliumweb
cd titilliumweb
wget https://fonts.google.com/download?family=Titillium%20Web -O titilliumweb.zip
unzip titilliumweb.zip
cd ../

echo ""
echo "${bldblu}                        **                        "
echo "${bldblu}                      **# **                      "
echo "${bldblu}                    **##### **                    "
echo "${bldblu}                  **######### **                  "
echo "${bldblu}                **############# **                "
echo "${bldblu}              **################# **              "
echo "${bldblu}            **##################### **            "
echo "${bldblu}          **###***      *****######## **          "
echo "${bldblu}        **##**        ***    ***####### **        "
echo "${bldblu}      **##**         *###*      ***###### **      "
echo "${bldblu}    **###*            ****         *****### **    "
echo "${bldblu}  **####*                     ***############ **  "
echo "${bldblu} **###**                    **#################** "
echo "${bldblu}  ****                     *##################**  "
echo "${bldblu}                          *#################**    "
echo "${bldblu}                         *|###############**      "
echo "${bldblu}                         *##############**        "
echo "${bldblu}                         *############**          "
echo "${bldblu}                         *##########**            "
echo "${bldblu}                         |########**              "
echo "${bldblu}                        *#######**                "
echo "${bldblu}                       * #####**                  "
echo "${bldblu}                      *#####**                    "
echo "${bldblu}                      ** #**                      "
echo "${bldblu}                        **                        "
echo ""

echo "komiti is fork of Koruri (https://github.com/koruri/koruri)"
echo "komiti を生成するには FontForge をインストールし、"
echo "最新の M+ 1p を mplus/ に展開した後、以下を実行してください"
echo "fontforge -lang=py -script komiti.py"
tput sgr0
