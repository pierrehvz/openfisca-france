# -*- coding: utf-8 -*-

from __future__ import division

import datetime

from numpy import maximum as max_, minimum as min_
from openfisca_core import columns, entities, reforms

from .. import entities
from ..model.base import dated_function
from ..model.prelevements_obligatoires.impot_revenu import reductions_impot


# TODO: les baisses de charges n'ont pas été codées car annulées (toute ou en partie ?)
# par le Conseil constitutionnel


def build_reform(tax_benefit_system):
    Reform = reforms.make_reform(
        key = u'plfr2014',
        name = u'Projet de Loi de Finances Rectificative 2014',
        reference = tax_benefit_system,
        )
    reform = Reform()
    Variable = Reform.Variable

    class var1(Variable):
        column = columns.FloatCol
        entity_class = entities.FoyersFiscaux
        def function(self, simulation, period):
            grorep = simulation.legislation_at(period.start).ir.charges_deductibles.grorep
            return period, self.zeros() + grorep.max

    # reform.update_legislation.ir.xxx  # TODO raise ParameterNotFound
    reform.update_legislation.ir.charges_deductibles.grorep.max = 999
    return reform


if __name__ == '__main__':
    import openfisca_france
    tax_benefit_system = openfisca_france.init_tax_benefit_system()
    reform = build_reform(tax_benefit_system)
    year = 2014
    scenario = reform.new_scenario().init_single_entity(
        period = year,
        parent1 = dict(birth = datetime.date(year - 40, 1, 1)),
        )
    reform_simulation = scenario.new_simulation(debug = True)
    print reform_simulation.calculate('var1', '2014')
    print reform_simulation.calculate('var1', '2015')
    print reform_simulation.calculate('var1', '2099')
    print reform_simulation.calculate('var1', '1900')
    print reform_simulation.calculate('var1', '1890')
