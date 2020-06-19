pybioinformatics
================

Learning bioinformatics in python.

This GitHub repository has the Student materials for the UC Davis course MCB185: Computer Programming for Biologists. In each `Lesson` directory there is a `00README.md` file with the instructions for the lesson. You will also find some tutorial programs and programming exercises.

Notes on Macs
=============

Developer command line tools are not installed by default. You can get them by installing all of Xcode or installing just the command line tools. Type the following into your terminal to install just the command line tools.

	xcode-select --install

Notes on Ubuntu on Windows
==========================

## Finding Your Unix Home Directory From Windows ##

If you're using Ubuntu on Windows 10, your linux home directory is in an obscure place whose path is something like the one below.

C:\Users\yourname\AppData\Local\Packages\Canonical...\LocalState\rootfs\home\

In Windows, directory names are separated by backslash: \

In Linux, directory names are separated with forward slash: /

`yourname` is whatever your Windows user name is. It probably looks a little like your own name, but may be abbreviated. For example, my name is 'Ian Korf' but my Windows username is `ianko`.

`AppData` is a hidden folder. You can't see it, but you can type its name to get to it.

`Canoncial...` is a really long name that looks really strange. On my computer it looks like this:

	CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc

In order for you to get to your Linux home easily from Windows, you should create a Shortcut for it. Right click on the desktop and choose New->Shortcut. Now navigate to the directory above typing in AppData as necessary. When you get to your home folder, you can give the Shortcut a name. I call mine `ubuntu-home`.

## Finding Your Windows Home Directory From Linux ##

Getting to your Windows directory is much easier from Linux. Your `C` drive is in `/mnt/c`, so your Windows home is in `/mnt/C/Users/yourname`, where `yourname` is your Windows user name as mentioned previously. If you want to create an alias to your Windows desktop, use the following command from your Linux home directory

	ln -s /mnt/c/Users/yourname/Desktop ./windows-desktop

## Always Create Your Files in Linux ##

You may like double-clicking your files in Windows to open them in your text editor (for example Notepad++). That's fine, but NEVER CREATE FILES IN WINDOWS. They will become invisible in Linux (and also have the wrong kind of line endings). Let's make sure we get the point.

NEVER CREATE FILES IN WINDOWS!

Really, please never do that. Instead, create the file in Linux, even if it's empty. The following command will create an empty file called `foo.txt` which you can then double-click and edit in your editor of choice.

	touch foo.txt

## Windows-Linux File Permission Woes ##

After editing a file with a Windows file editor, like Notepad++, the permissions of the file may change the next time your reboot your computer. This can be very annoying. However, it is simple to fix. The following command will make all of your python files readable, writable, and executable to you (just readable and executable for others).

	chmod 755 *.py



