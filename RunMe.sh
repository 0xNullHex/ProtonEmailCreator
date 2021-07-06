RED="\e[31m"
GREEN="\e[32m"
ENDCOLOR="\e[0m"
BOLD="\e[1m"

# Install selenium
echo -e "Checking ${BOLD}Selenium${ENDCOLOR}...\n"
pip install selenium
if [[ $? -ne 0 ]]; then
    echo -e "${RED}Selenium could be installed !$ENDCOLOR"
    exit 1
fi

echo -e "\n${GREEN}Dependency checked !$ENDCOLOR"
echo -e "Executing script... \n"

python GmailBot.py
