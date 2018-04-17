# pins = {'ADC1'   : 'X5' ,  # GCaMP
#         'ADC2'   : 'X6' ,  # RFP
#         'DI1'    : 'X11',  # Behavioural event
#         'DI2'    : 'X12',  # Sync
#         'LED1'   : 'X1' ,  # 475nm LED
#         'LED2'   : 'X2' }  # 405nm LED

pins = {'ADC1'   : 'X5' ,  # GCaMP
        'ADC2'   : 'X6' ,  # RFP
        'DI1'    : 'X1',  # Behavioural event
        'DI2'    : 'X2',  # Sync
        'LED1'   : 'X11' ,  # 475nm LED
        'LED2'   : 'X12' }  # 405nm LED

history_dur   = 10     # Duration of plotted signal history (seconds)
triggered_dur = [-3,6] # Window duration for event triggered signals (seconds pre, post)

update_interval = 20 # Interval between calls to update function (ms).