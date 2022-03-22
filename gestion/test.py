import time
import modules
from modules import database
from modules import node

print( 1)
bp = database.Blueprint()
bp["project"] = database.Project()
bp["root"] = database.Path()
doc = database.Document.create_from_blueprint( bp )

doc["project"] = "baboo"
doc["root"] = "/home/arno"
doc.set_all_values()

node.map_to_self( doc.as_datatype( "root" ) )

# ~ print(doc)
