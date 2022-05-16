# RapidMiner sklearn Extension #
This extension bundles algorithms from scikit-learn as RapidMiner operators. Users can install an extension from RapidMiner marketplace and have operators
in their operator tree available. This extension does not claim completeness and will update over time.

Since this extension uses python based operators it will always rely on RapidMiner's python extension to be installed.
It further requires sklearn to be installed in the used python environment.

## How to install ##

Please use the .jar provided on the RapidMiner marketplace if you want to use this extension.

## How to compile ##

You only need to compile this extension yourself if you want to add additional operators.
After adding more files you can run compile.py to create the corresponding .pyop files. Afterwards you have to go
to RapidMiner Studio and right click on the rapidminer-sklearn folder. You can then choose 'create extension'
to create the .jar file which can be loaded into other RapidMiner execution environments.

## Author ##
Main author: Martin Schmitz <mschmitz@rapidminer.com> for RapidMiner - rapidminer.com