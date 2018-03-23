import sys # you need this library since it captures the CLI parameters

print(sys.argv)
args = sys.argv
print "%s is going to %s on %s" % (args[1],args[2],args[3])

"""
Run this script using - python cli_args <param1> <param2>
Try running this with spaces in the first param , see what happens
    - python cli_args.py Ganesh Prasath Paris
    - python cli_args.py "Doctor Who" 1980
    - python cli_args.py 'Ganesh Prasath' Paris

Try separating the parameters using comma
    - python cli_args.py "Captain Piccard",Risa
Try giving various values. Try giving just one value

Try using "" for one value ( python cli_args.py Ross "" )
Try using '' for one value
"""

