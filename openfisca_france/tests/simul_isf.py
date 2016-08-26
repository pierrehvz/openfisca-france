# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:38:02 2016

@author: p.havez
"""

from openfisca_france import FranceTaxBenefitSystem
tax_benefit_system = FranceTaxBenefitSystem()


scenario = tax_benefit_system.new_scenario().init_single_entity(
    parent1=dict(salaire_de_base=150000,
                 age = 60,
                 ),
    period=2016,
    foyer_fiscal = dict(
        b1ab = 2000000,
        b1bc = 100000,
        b1be = 100000,
        b1cf = 100000,
        b2nc = 1000
        ),
    )
simulation = scenario.new_simulation(trace=True)
simulation.calculate('isf_apres_plaf', 2016, print_trace=True)


#scenario = tax_benefit_system.new_scenario().init_single_entity(
#    parent1 = dict(
#        #salaire_de_base = 150000,
#        age = 60,
#        ),
#    period = 2016,
##    foyer_fiscal = dict(
##        b1ab = 2000000,
##        b1bc = 100000,
##        b1be = 100000,
##        b1cf = 100000,
##        b2nc = 1000
##        ),
#    )
#simulation = scenario.new_simulation(trace=True)
#simulation.calculate('isf_tot', 2016, print_trace=True)
#
#

## scenario de base, github #
#scenario = tax_benefit_system.new_scenario().init_single_entity(
#    parent1=dict(salaire_de_base=25000),
#    period=2014,
#    )
#simulation = scenario.new_simulation(trace=True)
#simulation.calculate('irpp', 2014, print_trace=True)