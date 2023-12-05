:: Download and build PDCurses
@echo on

curl -L -o PDCurses.zip https://codeload.github.com/wmcbrine/PDCurses/zip/refs/tags/3.9
if errorlevel 1 exit /B 1

tar -xf PDCurses.zip --strip-components=1
if errorlevel 1 exit /B 1

git apply --verbose --binary pdcurses.diff
if errorlevel 1 exit /B 1

cd wincon
if errorlevel 1 exit /B 1

nmake.exe /nologo -f Makefile.vc WIDE=Y UTF8=Y all
if errorlevel 1 exit /B 1
