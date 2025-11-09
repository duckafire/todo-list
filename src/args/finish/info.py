from sys import exit

from ... import info

# Print And Exit
def pae(msg):
    print(msg)
    exit()


def default():
    pae( \
f"""{info.header()}
Try: `{info.name()} -h`

{info.copyright()}

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute
it under certain conditions.
""")


def help():
    pae( \
f"""{info.name()} [ --help | --license | --version ]
{info.name()} [ --verbose ] [ --replace ]

-h --help      displays this error message.
-l --license   displays the program license.
-r --replace   specifics that the `todo-list` must be replaced (if it exists).
-V --verbose   enables the verbose mode (it display a lot of information in runtime).
-v --version   displays the program version.
""")


def license():
    pae( \
f"""{info.copyright()}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
""")


def version():
    pae(info.version())


__all__ = ["help", "license", "version"]
