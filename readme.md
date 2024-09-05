
Mac

Run this command to activate conda in env: 
    conda activate /Users/neilgawande/ONEAPE/Math/mathenv

Note* prependpath/mathenv can vary depending on your environment.

Make sure Jupyter recognizes Kernel:
    conda activate /Users/neilgawande/ONEAPE/Math/mathenv
    conda install ipykernel
    python -m ipykernel install --user --name=mathenv --display-name="Python (mathenv)"


Windows
conda create --prefix C:/ONEAPE/Math/mathenv python=3.12 numpy pandas matplotlib
conda activate C:\ONEAPE\Math\mathenv
