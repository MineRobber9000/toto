import tkinter, json
import os.path as fs

class Application(tkinter.Frame):
	def __init__(self,parent=None):
		print("init app frame")
		super(Application,self).__init__(parent)
		self.parent = parent
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		print("entry widget")
		self.entry = tkinter.Entry(self)
		self.entry.pack(side="top")
		print("listbox widget")
		self.list = tkinter.Listbox(self)
		print("call loadTasks")
		self.loadTasks()
		self.pack(side="bottom")
		print("add/resolve buttons")
		self.add_task_button = tkinter.Button(self,text="Add",command=self.add_task)
		self.add_task_button.pack(side="bottom")
		self.resolve_button = tkinter.Button(self,text="Resolve",command=self.resolve)
		self.resolve_button.pack(side="bottom")

	def loadTasks(self):
		i = 1
		if fs.exists(fs.expanduser("~/.tototasks")):
			print("tasks file exists, open it")
			with open(fs.expanduser("~/.tototasks")) as f:
				self.tasks = json.load(f)["tasks"]
				print("{!r}".format(self.tasks))
				for entry in self.tasks:
					self.list.insert(i,entry)
					i+=1
		else:
			print("no tasks file!")
			self.tasks = []

	def add_task(self,*args,**kwargs):
		self.tasks.append(self.entry.get())
		with open(fs.expanduser("~/.tototasks"),"w") as f:
			json.dump(dict(tasks=self.tasks),f)

	def resolve(self,*args,**kwargs):
		print("resolve")

app = tkinter.Tk()
app.title("TOTO")
root = Application(app)
#print(dir(app))
