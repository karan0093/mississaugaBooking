import automate

def call(arg1, arg2, arg3):
	run = automate.Automate(arg1,arg2,arg3)
	run.runSequence()
	print("success!")

def call2(arg1, arg2, arg3):
	run = automate.Automate(arg1,arg2,arg3)
	run.runSequence()
	print("success!")
