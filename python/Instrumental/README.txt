1) pip install instrumental-lib (https://instrumental-lib.readthedocs.io/en/stable/)
2) pip install -U pyvisa (https://pyvisa.readthedocs.io/en/latest/)
3) Download and install VISA drivers: https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html#442805
4) Add
```class Wavepro725Zi(LeCroyScope):

    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('LeCroy', 'WP725ZI', RESOLUTION['8bits'], ANALOGUE_CHANNELS['4'])```
	to lecroy.py
5) Add lecroy.py to ".../site-packages/instrumental/drivers/scopes" folder
6) Add
```(('scopes.lecroy', {
        'params': ['visa_address'],
        'classes': ['Waverunner625Zi', 'Wavepro404HD', 'Wavepro725Zi'],
        'imports': ['pyvisa', 'visa'],
        'visa_info': {
            'Waverunner625Zi': ('LECROY', ['WR625ZI']),
            'Wavepro404HD': ('LECROY', ['WP404HD']),
            'Wavepro725Zi': ('LECROY', ['WP725ZI']),
        },
    })```
	to ".../site-packages/instrumental/driver_info.py/"

Usage: https://instrumental-lib.readthedocs.io/en/stable/instruments.html