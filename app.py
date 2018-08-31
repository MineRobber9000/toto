import tkinter, json
import os.path as fs

class Application(tkinter.Frame):
	def __init__(self,parent=None):
#		print("init app frame")
		super(Application,self).__init__(parent)
		self.parent = parent
		self.pack()
		self.create_widgets()

	def create_widgets(self):
#		print("entry widget")
		self.entry = tkinter.Entry(self)
		self.entry.pack()
#		print("listbox widget")
		self.list = tkinter.Listbox(self,selectmode=tkinter.SINGLE)
#		print("call loadTasks")
		self.loadTasks()
		self.list.pack()
#		print("add/resolve buttons")
		self.button_frame = tkinter.Frame(self)
		self.button_frame.pack(side="bottom")
		self.add_task_button = tkinter.Button(self.button_frame,text="Add",command=self.add_task)
		self.add_task_button.pack(side="left")
		self.resolve_button = tkinter.Button(self.button_frame,text="Resolve",command=self.resolve)
		self.resolve_button.pack(side="left")

	def loadTasks(self):
		if fs.exists(fs.expanduser("~/.tototasks")):
#			print("tasks file exists, open it")
			with open(fs.expanduser("~/.tototasks")) as f:
				self.tasks = json.load(f)["tasks"]
#				print("{!r}".format(self.tasks))
		else:
#			print("no tasks file!")
			self.tasks = []
		self.redoListbox()

	def add_task(self,*args,**kwargs):
#		print("add_task "+self.entry.get())
		self.tasks.append(self.entry.get())
		self.saveTasks()
		self.redoListbox()

	def redoListbox(self):
		self.list.delete(0,"end")
		for entry in self.tasks:
			self.list.insert("end",entry)

	def getSelectedTask(self):
		return self.tasks[self.list.curselection()[0]]

	def resolve(self,*args,**kwargs):
#		print("resolve")
		self.tasks.remove(self.getSelectedTask())
		self.saveTasks()
		self.redoListbox()

	def saveTasks(self):
		with open(fs.expanduser("~/.tototasks"),"w") as f:
			json.dump(dict(tasks=self.tasks),f)

app = tkinter.Tk()
app.title("TOTO")
root = Application(app)
#print(dir(app))
