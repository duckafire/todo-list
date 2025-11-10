[cli-wiki]: https://en.wikipedia.org/wiki/Command-line_interface "What is a cli?"
[path-wiki]: https://en.wikipedia.org/wiki/PATH_(variable) "Wikipedia"
[git-home]: https://git-scm.com/ "Git website home"
[hub-download]: https://github.com/duckafire/todo-list/archive/refs/heads/main.zip "zip from gitHUB"
[lab-download]: https://gitlab.com/duckafire/todo-list/-/archive/main/todo-list-main.zip?ref_type=heads "zip from gitLAB"
[python-path]: http://stackoverflow.com/questions/76188316/ddg#76188371 "Understanding the PYTHONPATH variable"
[shebang]: https://en.wikipedia.org/wiki/Shebang_%28Unix%29 "Wikipedia"

## todo-list

This project has as aim to available a safe, easy, and fast way to manager *to do lists*
through the use of a terminal [cli][cli-wiki].

Python was chosen as base language to this project because of its alignment to the
proposal of it (what they already were cited) and because of the high portability of
the language between different Operational System.

The code of this project aims to align it to the main conventions disseminated by the
community of that programming language, in order to welcome possible contributors that
can collaborate to the evolution of this project.



### Topics

* [Installing](#installing)
	* [Python](#python)
	* [Project](#project)
* [Executing](#executing)
* [How to use](#how-to-use)



### Installing

#### Python

As said earlier, this project was written using Python3, therefore, to execute it, it is
necessary to install its interpreter, what it can be done via the commands below:

```
# debian based
sudo apt install python3

# archlinux based
sudo pacman -S python3

# fedora based
sudo dnf install python3
```

If your Operational System do not support the commands above, you have:

* Access the documentation of your Operational System, with emphasize in its package
  manager.

* Download the interpreter via this URL: <https://www.python.org/downloads/>

After this, access the terminal (like: CMD; xTerm) of your Operational System and
execute the command below:

```
python3 --version
```

If the interpreter version was shown, it means that the interpreter was installed with
success. Else, if an error similar with `Command not found: "python3"` was shown, it
means that anything wrong occurred. There are two main reasons to it.

1. The interpreter executable has other name.
1. The interpreter was not correctly installed.

In first case, try replacing `python3` to `python`. Case it do not work, query the
interpreter documentation and/or check the interpreter installation directory.

In second case, try checking the values of the `PATH` variable of your Operational
System (run `echo $PATH` or `echo %PATH%`) and/or query the documentation of it, in
order to obtain solutions already documented about the problem.

> [!NOTE]
> [What is the `PATH` variable?][path-wiki]



#### Project

Now it is time to download this project. You can to do this of two ways:

Installing via [Git][git-home] through of a of the commands below (via terminal):

```
# from gitHUB
git clone https://github.com/duckafire/todo-list.git

# from gitLAB
git clone https://gitlab.com/duckafire/todo-list.git
```

Or through of the URL below:

* [From GitHub][hub-download]
* [From GitLab][lab-download]

> [!TIP]
> Remember of to extract the downloaded file. Your Operational System probably will
> have a native tool to do it. Case it do not have, you can query its documentation,
> in search of packages/programs to execute this work.



### Executing

Now that all it is in your machine, you can access the directory of this projects (that
it had downloaded earlier) via of a terminal.

> [!TIP]
> Use the command `cd`. Try `cd -h` or `cd -?`.

After this, execute the command below:

```
python3 ./todo-list.py --version
```

> [!IMPORTANT]
> Remember you: the interpreter name can be different.

> [!TIP]
> If your Operational System supports [*shebang*][shebang], as systems *Unix-like* and
> *Linux-like*, you can use only:
>
> ```
> ./todo-list.py --version
> ```
>
> But you still will need of the Python interpreter.

This will prints the program version. Execute `python3 todo-list.py -h` to obtain help
information or read the sections below (**I recommend**).

> [!TIP]
> Having that to go to the project installation directory every time that you want to
> the this program looks like boring and low. Happily, there is how to improve this
> through the use of the `PYTHONPATH` Environment Variable, but it is a long topic, so
> I will put a URL about it [here][python-path] to you.
> This will not work if you using the [*shebang*][shebang], because it depends of other
> environment variable, the [`PATH`][path-wiki].



### How to use

Now that you know how to execute this project, we will talk about how to use the program.
Like other [CLI programs][cli-wiki], this has itself *flags*, you can run the command
below to list them (together with their description):

```
python3 ./todo-list.py --help
```

There are two groups of flags, they are:

* Infomation flags:
	* They must be the fist argument of the program.
	* They display an information message, and they finish the program with success.
	* Program will ignore totally other argument (>=2nd) when one of them is used.
	* Program will generate an error, and it will fail, if one of them is used out of
	  the first position.

* Action flags:
	* They allow to control behaviors, process, and other things related with the
	  *to do list* management.
	* They can be placed in any argument position.
	* Repeat them, in the same call, it will generate fatal errors.
	* Some of them must require an argument, that it must to be placed after it
	  (e.g: `--flag arg`).

Well, it is all. It is easy, isn't it?
