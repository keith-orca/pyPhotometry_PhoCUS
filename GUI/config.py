VERSION = '0.3.2' # Version number of pyPhotometry.

# ----------------------------------------------------------------------------------------
# GUI Config
# ----------------------------------------------------------------------------------------

history_dur   = 10       # Duration of plotted signal history (seconds)
triggered_dur = [-3,6.9] # Window duration for event triggered signals (seconds pre, post)
update_interval = 5      # Interval between calls to update function (ms).

default_LED_current = [10,10] # Channel [1, 2] (mA).

default_acquisition_mode = '2 colour continuous' # Valid values: '2 colour continuous', '1 colour time div.', '2 colour time div.'

default_filetype = 'ppd' # Valid values: 'ppd', 'csv'