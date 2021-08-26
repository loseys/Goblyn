
<h1 align="center">
  <br>
  <a href="https://github.com/loseys/Goblyn"><img src="https://user-images.githubusercontent.com/61597947/130886015-52e6f5a6-bf78-42bd-bda7-5f862faf2de8.png" width=150 height=140 lt="Goblyn"></a>
  <br>
  Goblyn
  <br>
</h1>

<h4 align="center">Metadata Enumeration</h4>

<p align="center">
  <a href="https://github.com/loseys/Goblyn/">
    <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux-yellow">
  </a>
  <a href="https://github.com/loseys/Goblyn/">
    <img src="https://img.shields.io/badge/version-v0.1-red">
  </a>
  <a href="https://github.com/loseys/Goblyn/">
      <img src="https://img.shields.io/badge/python-3.9-green.svg">
  </a>
</p>

![image](https://user-images.githubusercontent.com/61597947/130886515-1cc1291b-0aac-4ca4-82ec-e500215e4775.png)


### What's Goblyn?

Goblyn is a tool focused to enumeration and capture of website files metadata.

### How it works?

Goblyn will search for active directories in the website and so enumerate the files, if it find some file it will get the metadata of file.

### Why Goblyn?

- Supports multiple file types;
- Simple to use;
- Easy installation;
- Fast.

### Installing Goblyn


1. Download this repository and run:
```
sudo python3 setup.py install
```

2. Download the `exiftool`:
```
sudo apt install exiftool
```

3. Have fun :)

```
sudo goblyn [OPTIONS]
```

### How to use Goblyn?

You can use the `-help` argument to explore help banner of Goblyn.

Example of use:

```
sudo goblyn -t http://fma.if.usp.br/~amsilva/Livros/ -wl C:\Users\Lsy\Desktop\common.txt --file-types=pdf,docx,png
```
### Call for Contributions⚠️

If you finds this tool useful and wants to add some functionality, improve the code performance or improve something in the Goblyn, the best way to get it added is to submit a pull request.
