#scoring solution 
#usage: bash check.sh input solution_to_check file_with_score    
# UŻYWAĆ TYLKO PRZY 1 PROCESIE (inaczej może być przyps) to przez ten TEMP_CHECKER_FILE

tag=${1?"usage: bash check.sh input solution_to_check file_with_score"}

IN_FILE=$1
OUT_FILE=$2
SCORE_FILE=$3
cat $IN_FILE > TEMP_CHECKER_FILE
cat $OUT_FILE >> TEMP_CHECKER_FILE
./chk < TEMP_CHECKER_FILE > $SCORE_FILE
rm TEMP_CHECKER_FILE
