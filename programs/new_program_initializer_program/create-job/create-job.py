from shutil import copy
import os, sys, json

path = ".\\"
template_prog = "..\\Templates\\python_template.py"
directory = os.listdir(path)

#OPEN JOB PROJECT NUMBER FILE
try:
	with open(".\input.txt", "r") as inp:
		input_counter = 0
		for line in inp:
			input_counter = int(line)
		inp.close()
	print("Job counter file open successful...")
except:
	print("Unexpected error: When obtaining current job number: ", sys.exc_info()[0])
	raise

#CREATE JOB PROJECT FOLDER AND INITIALIZE FILES
try:
	with open(".\input.txt", "w") as inp:		
		job_numbers = []
		for file in directory:
			base=os.path.basename(file)
			if os.path.splitext(base)[0].startswith("job"):
				if not os.path.splitext(base)[1]:
					job_numbers.append(os.path.splitext(base)[0].split('-')[1])
		if (int(max(job_numbers))==input_counter):
			input_counter += 1
			new_job_folder = "{}job-{:04d}\\".format(path.replace("\\\\", "\\"), input_counter)
			os.mkdir(new_job_folder, 777)
			os.chdir(new_job_folder)
			copy(template_prog, new_job_folder)
			new_job_folder_list = os.listdir(new_job_folder)
			os.rename('python_template.py', "job-{:04d}.py".format(input_counter))		
			inp.write(str(input_counter))
		new_file = ""
		new_line = ""
		with open("job-{:04d}.py".format(input_counter), "r") as original:
			for line in original:
				new_line = line.replace("???!!!", "job-{:04d}".format(input_counter))
				new_file = "{}{}".format(new_file, new_line)
		with open("job-{:04d}.py".format(input_counter), "w") as modified:
			modified.write(new_file)
		original.close()
		modified.close()
	print("Job project folder creation successful...")
except:
	print("Unexpected error: When creating job project folder: ", sys.exc_info()[0])
	raise
	
print("\n\n Enter Job Project Details for Directory...\n\n")
in_type_sel = "uninitialized-variable"
in_jcat_sel = "uninitialized-variable"
in_desc_sel = "uninitialized-variable"
final_string = "\n{:04d},".format(input_counter)

try:
	with open("..\job_directory.txt", "a+") as inp:
		db = open("..\data_dictionaries.JSON")
		data_dicts = json.load(db)
		loaded_dict = {}
		counter = 0
	#PROJECT TYPES
		for ddict in data_dicts:
			for k, v in ddict.items():
				if k == "project types":
					loaded_dict = ddict["project types"]
		for k, v in loaded_dict.items():
			counter += 1
			print("{}) {}".format(k, v))
		typesel_isvalid = False
		while not typesel_isvalid:
			if in_type_sel == "uninitialized-variable":
				in_type_sel = input("\n\nSelect Job Project Type> ")
			else:
				in_type_sel = input("Select Job Project Type> ")
			if str(in_type_sel).isdigit() and int(in_type_sel) <= counter:
				typesel_isvalid = True
		final_string = "{}{},".format(final_string, loaded_dict[str(in_type_sel)])
	#JOB CATAGORIES
		for ddict in data_dicts:
			for k, v in ddict.items():
				if k == "job catagories":
					loaded_dict = ddict["job catagories"]
		for k, v in loaded_dict.items():
			counter += 1
			print("{}) {}".format(k, v))
		jcatsel_isvalid = False
		while not jcatsel_isvalid:
			if in_jcat_sel == "uninitialized-variable":
				in_jcat_sel = input("\n\nSelect Job Project Catagory> ")
			else:
				in_jcat_sel = input("Select Job Project Catagory> ")
			if str(in_jcat_sel).isdigit() and int(in_jcat_sel) <= counter:
				jcatsel_isvalid = True
		final_string = "{}{},".format(final_string, loaded_dict[str(in_jcat_sel)])
		db.close()
	#JOB DESCRIPTION
		desc_isvalid = False
		while not desc_isvalid:
			if in_desc_sel == "uninitialized-variable":
				in_desc_sel = input("\n\nWrite Job Project Description> ")
			else:
				in_desc_sel = input("Write Job Project Description> ")
			if not str(in_desc_sel):
				continue
			else:
				in_desc_sel2 = input("\n\n{}\n\nAre you happy with this input?>".format(in_desc_sel))
				if in_desc_sel2 in ["y", "yes", "Y", "YES"]:
					desc_isvalid = True
		final_string = "{}{},{}".format(final_string, in_desc_sel,"active")
		inp.write(final_string)
		new_file = ""
		with open("job-{:04d}.py".format(input_counter), "r") as original:
			for line in original:
				if "description" in line:
					line = '\"\"\"{}\"\"\"\n'.format(in_desc_sel)
				new_file = "{}{}".format(new_file, line)
		with open("job-{:04d}.py".format(input_counter), "w") as modified:
			modified.write(new_file)
except:
	db.close()
	print("Unexpected error: When updating job_directory: ", sys.exc_info()[0])
	raise
