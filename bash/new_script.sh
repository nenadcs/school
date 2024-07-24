#!/usr/bin/env bash
set -euo pipefail

filename=$1

touch "./$filename.sh"

script="./$filename.sh"

chmod u+x $script

echo "#!/usr/bin/env bash" >> $script
echo "set -euo pipefail" >> $script
echo "# don't really know if the pipefail thing is necessary" >> $script
echo "" >> $script
