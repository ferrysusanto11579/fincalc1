import pandas as pd
import numpy as np

class FinancialModelling():
    
    @staticmethod
    def calculate_dcf(base_revenue, base_revenue_unit
                      , revenue_growth, revenue_growth_terminal
                      , base_sharesout, sharesout_unit, sharesout_growth
                      , net_margin, fcf_margin
                      , num_of_years=10, terminal_year_multiple=12, discount_rate=0.125):
        ## Local functions
        def _get_actual_value_by_unit(base, unit):
            if unit.lower() == 'billion':
                return base * 10**9
            if unit.lower() == 'million':
                return base * 10**6
            return base
        def _get_periods_growths(growths, n_periods, growths_end=None):
            if growths_end is None:
                return np.array([growths] * n_periods)
            return np.linspace(growths, growths_end, n_periods)
        def _get_period_values_by_growths(base, periods_growths):
            periods_multiple = np.cumprod(1 + periods_growths)
            return base * periods_multiple
        
        ## Revenue - Growth & estimation
        revenue_growth_periods = _get_periods_growths(revenue_growth, num_of_years, growths_end=revenue_growth_terminal)
        revenue = _get_actual_value_by_unit(base_revenue, base_revenue_unit)
        revenue_periods = _get_period_values_by_growths(revenue, revenue_growth_periods)
        
        ## Shares outstanding - Growth & estimation
        sharesout_growth_periods = _get_periods_growths(sharesout_growth, num_of_years, growths_end=None)
        sharesout = _get_actual_value_by_unit(base_sharesout, sharesout_unit)
        sharesout_periods = _get_period_values_by_growths(sharesout, sharesout_growth_periods)
        
        ## Calculate periods discount rate
        periods = np.arange(1, num_of_years+1)
        discountrate_periods = 1. / (1+discount_rate)**periods
        
        ## Calculate DCF - by EPS & FCF
        def _perform_dcf_calculations(cashflow_periods, cashflow_margin, sharesout_periods, discountrate_periods, terminal_year_multiple):
            netcashflow_periods = cashflow_periods * cashflow_margin
            netcashflow_ps_periods = netcashflow_periods / sharesout_periods
            netcashflow_ps_disc_periods = netcashflow_ps_periods * discountrate_periods
            netcashflow_ps_disc = netcashflow_ps_disc_periods.sum()
            netcashflow_ps_disc_terminal = netcashflow_ps_disc_periods[-1] * terminal_year_multiple
            return {'calculations':{'totalcashflow': cashflow_periods
                                    , 'net': netcashflow_periods
                                    , 'net_ps': netcashflow_ps_periods
                                    , 'net_ps_disc': netcashflow_ps_disc_periods},
                    'result': {'growth':netcashflow_ps_disc
                               , 'terminal':netcashflow_ps_disc_terminal}
                   }
        dcf_eps = _perform_dcf_calculations(revenue_periods, net_margin, sharesout_periods, discountrate_periods, terminal_year_multiple)
        dcf_fcf = _perform_dcf_calculations(revenue_periods, fcf_margin, sharesout_periods, discountrate_periods, terminal_year_multiple)
        
        return {
            'input': { 'base_revenue': base_revenue,
                        'base_revenue_unit': base_revenue_unit,
                        'revenue_growth': revenue_growth,
                        'revenue_growth_terminal': revenue_growth_terminal,
                        'base_sharesout': base_sharesout,
                        'sharesout_unit': sharesout_unit,
                        'sharesout_growth': sharesout_growth,
                        'net_margin': net_margin,
                        'fcf_margin': fcf_margin,
                        'num_of_years': num_of_years,
                        'terminal_year_multiple': terminal_year_multiple,
                        'discount_rate': discount_rate},
            'calculations': { 'revenue_growths': revenue_growth_periods,
                              'revenue_estimated': revenue_periods,
                              'sharesout_growths': sharesout_growth_periods,
                              'sharesout_estimated': sharesout_periods,
                              'net_margin': np.array([net_margin]*num_of_years),
                              'netincome': dcf_eps['calculations']['net'],
                              'eps': dcf_eps['calculations']['net_ps'],
                              'eps_disc': dcf_eps['calculations']['net_ps_disc'],
                              'fcf_margin': np.array([fcf_margin]*num_of_years),
                              'fcf': dcf_fcf['calculations']['net'],
                              'fcf_ps': dcf_fcf['calculations']['net_ps'],
                              'fcf_ps_disc': dcf_fcf['calculations']['net'],},
            'result': { 'eps': dcf_eps['result'],
                        'fcf': dcf_fcf['result'],},
        }
