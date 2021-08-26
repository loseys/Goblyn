"""
Some banners.
"""


class Colors:
    blue = '\33[34m'
    green = '\033[92m'
    red = '\033[91m'
    end_color = '\033[0m'
    yellow = '\33[33m'
    purple = '\33[35m'
    violet = '\33[35m'
    grey = '\33[90m'


def banner_0():
    sg = Colors.green
    eg = Colors.end_color
    sr = Colors.red
    er = Colors.end_color
    sy = Colors.yellow
    ey = Colors.end_color

    b0 = (rf'''
                                          {sg},      ,{eg}
       {sy}___      _     _ {ey}                 {sg}/(.-""-.)\{eg}
      {sy}/ _ \___ | |__ | |_   _ _ __{ey}    {sg}\  \/      \/  /|{eg}
     {sy}/ /_\/ _ \| '_ \| | | | | '_ \{ey}  {sg}| \ / =.  .= \ / |{eg}  
    {sy}/ /_\\ (_) | |_) | | |_| | | | |{ey}  {sg}( \   {eg}{sr}o{er}{sg}\/{eg}{sr}o{er}   {sg}/ )/{eg}
    {sy}\____/\___/|_.__/|_|\__, |_| |_|{ey}  {sg}\_, '-/  \-' ,_/{eg}
                         {sy}|___/{ey}                                       
                                {Colors.grey}v0.1, Author: Loseys{Colors.end_color}
     ''')
    print(b0)


def banner_1(target, time, ftypes):
    sr = Colors.red
    sb = Colors.green
    ec = Colors.end_color
    b1 = f'''
  {sr}[{ec}?{sr}]{ec} {sb}Target:{ec} {target}
  {sr}[{ec}?{sr}]{ec} {sb}Current Time:{ec} {time}
  {sr}[{ec}?{sr}]{ec} {sb}File Types:{ec} {ftypes}
    '''
    print(b1)


def banner_2():
    bhelp = ('''
    NAME
            Goblyn - Metadata Enumeration.
    
    SYNOPSIS
            Goblyn [-t, --target] <URL> [-wl, --wordlist] <path> [--file-types=<...>] [OPTIONS]...
    
    DESCRIPTION
            Goblyn is a tool focused to enumeration and capture of website files metadata.
    
            -help
                    Shows this help page.
    
            -t, --target
                    Select the website target.
    
            -o <file>, --output <file>
                    Send the metadata results to a file.
    
            -wl <file>, --word-list <file>
                    Select a wordlist.
    
            --file-types=ALL
                    Search for all file types.
    
            --file-types=PNG,JPG,DOCX
                    Search for specifics file types.
    
            --user-agent="Goblyn"
                    Specify the user-agent hearder.
    
            -d <seconds>, --delay <seconds>
                    Delay time for each request.
                    
            --time-out=<seconds>
                    Time out for each request. Default is two seconds.
    ''')
    print(bhelp)


def banner_3(link):
    print(f"""  
  [i] Scaning: {link}
""")


def banner_4(msg):
    sg = Colors.green
    eg = Colors.end_color
    sr = Colors.red
    er = Colors.end_color
    sy = Colors.yellow
    ey = Colors.end_color

    b0 = (rf'''
                                          {sg},      ,{eg}
       {sy}___      _     _ {ey}                 {sg}/(.-""-.)\{eg}
      {sy}/ _ \___ | |__ | |_   _ _ __{ey}    {sg}\  \/      \/  /|{eg}
     {sy}/ /_\/ _ \| '_ \| | | | | '_ \{ey}  {sg}| \ / =.  .= \ / |{eg}  
    {sy}/ /_\\ (_) | |_) | | |_| | | | |{ey}  {sg}( \   {eg}{sr}o{er}{sg}\/{eg}{sr}o{er}   {sg}/ )/{eg}
    {sy}\____/\___/|_.__/|_|\__, |_| |_|{ey}  {sg}\_, '-/  \-' ,_/{eg}
                         {sy}|___/{ey}                                       
                                {Colors.grey}v0.1, Author: Loseys{Colors.end_color}
    
  {sr}[{er}!{sr}]{er} {sr}Error:{er} {msg} ''')
    print(b0)
