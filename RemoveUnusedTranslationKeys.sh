path_to_project=../path/to/project
RED='\033[0;31m'
GREEN='\033[0;32m'

rm notfoundfinal.json
rm foundfinal.json

touch temp.json
touch foundfinal.json
touch notfound.json
touch notfoundfinal.json

while IFS=, read -r key value
do
    if grep -r -q --include=\*.{js,html,json} --exclude-dir={node_modules,locale} $key $path_to_project; then
        # write in new json
        echo "$key" >> temp.json
        echo -e "${GREEN} $key was found !"
    else
        echo -e "${RED} $key not found"
        echo "$key" >> notfound.json
    fi

done < data.csv

#remove new lines
cat temp.json | tr -d '\r' >> foundfinal.json
cat notfound.json | tr -d '\r' >> notfoundfinal.json

rm temp.json
rm notfound.json

echo -e "---------------- DONE -------------------"
# stop auto closing
# sleep 300