trap ctrl_c INT
function ctrl_c()
{
	pkill -9 -P $$
}


#  USAGE cores, input_file, compiled_program 
#  to puszcza imp.py na wielu wątkach (sprawdzcie imp.py po szczegóły)

cores=$1
input=$2
who=$3
for((i=1;i<=$cores;i++)); do
	python3 imp.py $i $input $who &
done
wait
