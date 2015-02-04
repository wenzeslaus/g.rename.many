#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################################################################
#
# MODULE:       g.rename.multi
# AUTHOR(S):    Vaclav Petras (wenzeslaus gmail.com)
# PURPOSE:      Wrapper for g.rename
# COPYRIGHT:    (C) 2014 by authors above, and the GRASS Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
############################################################################

#%module
#% description: Renames data base element files in the user's current mapset.
#% keywords: general, map management, rename
#%end
#%option G_OPT_F_INPUT
#% key: rast
#% required: yes
#% multiple: no
#% label: File with rasters to be renamed
#% description: Format of the file is one raster per line. Old name first, new name second (separated by comma by default)
#% guisection: Raster
#%end
#% option G_OPT_F_SEP
#% required: yes
#% answer: comma
#% guisection: Source
#%end


import sys
import atexit

from grass.script.utils import parse_key_val, separator
from grass.script import core as gcore
from grass.exceptions import CalledModuleError


def main():
    options, flags = gcore.parser()

    rast = options['rast']
    sep = separator(options['separator'])

    with open(rast) as rasters_file:
        for line in rasters_file:
            line = line.strip()
            names = line.split(sep)
            if len(names) != 2:
                gcore.fatal(_("Cannot parse line <{line}> using separator"
                              " <{sep}> in file <{file}>")
                            .format(line=line, sep=sep, file=rast))
            gcore.run_command('g.rename', rast=names)


if __name__ == "__main__":
    sys.exit(main())
