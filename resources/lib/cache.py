#/*
# *
# * TuneIn Radio for Kodi.
# *
# * Copyright (C) 2015 Brian Hornsby
# *
# * This program is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation, either version 3 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program.  If not, see <http://www.gnu.org/licenses/>.
# *
# */

import os
import time

class Cache:
    def __init__(self, path, filename, useUtf8=False, max=None):
        if not os.path.exists(path):
            os.makedirs(path)
        self.cachedb = os.path.join(path, filename)
        self.max = max
        if (useUtf8):
            self.encoding = 'utf-8'
        else:
            self.encoding = None

    def add(self, item, field=None):
        cache = self.get()
        if cache.count(item) > 0:
            return False
        if field is not None:
            for row in cache:
                if row[field] == item[field]:
                    return False
        if self.max and len(cache) >= self.max:
            cache.pop(0)
        cache.append(item)
        open(self.cachedb, 'w', encoding=self.encoding).write(repr(cache))
        return True

    def get(self):
        if os.path.isfile(self.cachedb):
            return eval(open(self.cachedb, 'r', encoding=self.encoding).read())
        return []

    def remove(self, item):
        cache = self.get()
        if cache.count(item) == 0:
            return
        cache.remove(item)
        open(self.cachedb, 'w', encoding=self.encoding).write(repr(cache))
        return

    def len(self):
        cache = self.get()
        return len(cache)

    def clear(self):
        cache = []
        open(self.cachedb, 'w', encoding=self.encoding).write(repr(cache))
        return

    def lastupdate(self):
        if os.path.isfile(self.cachedb):
            return time.time() - os.path.getmtime(self.cachedb)
        return None
