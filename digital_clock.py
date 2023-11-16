import display_number as dm
import sys, time, subprocess

try:
    while True:
        #print('\n')
        #time.sleep(1)
        current_time = time.localtime()
        
        hours = str(current_time.tm_hour % 24)
        if hours == '0':
            hours = '24'
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)
        
        h_digits = dm.get_number_str(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()
        
        m_digits = dm.get_number_str(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()
        
        s_digits = dm.get_number_str(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()
        
        print(h_top_row    + '   ' + m_top_row    + '   ' + s_top_row, flush=True)
        print(h_middle_row + ' * ' + m_middle_row + ' * ' + s_middle_row, flush=True)
        print(h_bottom_row + ' * ' + m_bottom_row + ' * ' + s_bottom_row, flush=True)
        subprocess.call('clear', shell=True)
except KeyboardInterrupt:
    sys.exit()