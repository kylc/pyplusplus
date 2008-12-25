# Copyright 2004-2008 Roman Yakovenko.
# Distributed under the Boost Software License, Version 1.0. (See
# accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt)

import os
import code_creator


class name_mapping_t(code_creator.code_creator_t):
    """creates dictionery { [un]decorated name : [un]decorated name }"""

    def __init__( self, exported_symbols ):
        code_creator.code_creator_t.__init__(self)
        self._exported_symbols = exported_symbols


    def _create_impl(self):
        tmpl = '"%s" : "%s", '
        items_decorated = []
        items_undecorated = []
        for blob, undecorated in self._exported_symbols.iteritems():
            items_decorated.append( tmpl % ( blob, undecorated ) )
            items_undecorated.append( tmpl % ( undecorated, blob ) )

        result = []
        result.append('%s.undecorated_names = {#mapping between decorated and undecorated names' % self._dictionary_var_name ]
        for s in items_undecorated:
            result.append( self.indent( s ) )
        for s in items_decorated:
            result.append( self.indent( s ) )
        result.append( '}' )
        return os.linesep.join( result )


    def _get_system_headers_impl( self ):
        return []


if __name__ == '__main__':
    data = { 'a' : 'AA', 'b' : 'BB' }
    nm = name_mapping_t( 'name_mapping', data )
    print nm.create()
