date +'FORMAT'
 
### mm/dd/yyyy ###
date +'%d/%m/%Y'
 
## Time in 12 hr format ###
date +'%r'
 
## backup dir format ##
backup_dir=$(date +'%d/%m/%Y')
echo "Backup dir for today: /nas04/backups/${backup_dir}"

echo `date`
