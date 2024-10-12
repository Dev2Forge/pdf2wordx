import subprocess
import sys
import os
try:
    import pdf2docx
except ModuleNotFoundError:
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdf2docx', '--user'])
        import pdf2docx
    except subprocess.CalledProcessError as e:
        with open('log.log', 'a', encoding='utf-8') as log:
            log.write(f'Failed to install pdf2docx: {e}\n')
            sys.exit(1)
    except Exception as e:
        with open('log.log', 'a', encoding='utf-8') as log:
            log.write(f'Error running main script: {e}\n')
        sys.exit(1)

import main
main.run()
