cd setup

eval "$(mamba shell hook --shell bash)"

PM="mamba"
if ! command -v mamba &> /dev/null; then
    PM="conda"
fi

./01.stagein.sh

$PM env list | grep -q 'BigWig' || bash ./00.install_dependencies.sh



cd ../