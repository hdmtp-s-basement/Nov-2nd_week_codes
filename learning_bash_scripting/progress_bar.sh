: '
i=1
sp="/-\|"
echo -n ' '
while true
do
    printf "\b${sp:i++%${#sp}:1}"
done
'

echo -ne '|||                       [20%]\r'
# some task
sleep 2
echo -ne '|||||||                   [40%]\r'
# some task
sleep 2
echo -ne '||||||||||||||            [60%]\r'
# some task
sleep 2
echo -ne '|||||||||||||||||||||||   [80%]\r'
# some task
sleep 2
echo -ne '||||||||||||||||||||||||||[100%]\r'
echo -ne 'Success!\n'
