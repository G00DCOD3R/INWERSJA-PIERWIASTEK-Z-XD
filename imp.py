import sys, os

#   USAGE: 
	#   pisze po polsku, bo i tak nikt tego nie będzie nigdy używał
	#   ten program w kółko puszcza binarkę i jak wynik się poprawi to wypisuje wynik
	#   robicie python3 imp.py CORE IN BINARKA
	#   np. 
	#   python3 imp.py 1 a.in a
	#   jak nie puszczacie na wielu rdzeniach to wpisujcie 1
	#   fajnie jakby checkerka była skompilowana do ./chk, jak nie to zmieńcie tam gdzie nie będzie działać (~36 linijki)
	
	#   to wam zapisuje besta w __solN.sol, gdzie N to numer wątku
	#   poprzedniego besta zapisuje w __COPY_SOLN.sol, gdzie N to numer wątku
	#   poprzedni best jest potrzebny jakbyście zbreakowali w czasie przepisywania current besta do pliku (to jest kopia)

if __name__ == "__main__":
	core = int(sys.argv[1])
	BIN = "./" + sys.argv[3]
	IN = "TEMP_INPUT_FILE" + str(core)
	OUT = "TEMP_OUTPUT_FILE" + str(core)
	os.system("cp " + sys.argv[2] + " " + IN)
	shift = " " * 40 *  (core-1)
	#tutaj shifta trzeba zmienić w razie potrzeby na więcej spacji, żeby w osobnych kolumnach to działało 
	
	best = 0
	SOL = "__sol" + str(core) + ".sol"
	reps = 1
	co_ile_progress = 1000  # tutaj trzeba zmienić, żeby progress widzieć w miarę na bieżąco 
	
	while True:
		reps += 1
		if(reps % co_ile_progress == 0): 
			print(shift + "progress: " + str(reps // co_ile_progress))
		
			
		os.system(BIN + " < " + IN + " > " + OUT)
		#   os.system("bash check.sh " + IN + " " + OUT + " _score" + str(core))
		TEMP_FILE = "TEMP_CHECKER_FILE" + str(core)
		SCORE_FILE = "_score" + str(core)
		
		os.system("cat " + IN + " > " + TEMP_FILE)
		os.system("cat " + OUT + " >> " + TEMP_FILE)
		os.system("./chk < " + TEMP_FILE + " > " + SCORE_FILE)
		# jeśli wam tutaj nie działa, to binarka checkerki musi być skompilowana do ./chk albo zmieńcie po prostu
		
		cur_file = open(SCORE_FILE, "r")
		cur_score = int(cur_file.read())
		if(best < cur_score):
			print(shift + str(best) + " -> " + str(cur_score) + " (+" + str(cur_score - best) + ")")
			best = cur_score
			os.system("cp " + SOL + " __COPY_SOL" + str(core) + ".sol") # to żeby jak zbreakuje podczas kopiowania to nie było przypału 
			os.system("cp " + OUT + " " + SOL)
	
