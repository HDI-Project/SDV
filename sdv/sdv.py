# -*- coding: utf-8 -*-

"""Main module."""
import numpy as np

from DataNavigator import DataNavigator
from Modeler import Modeler
from Sampler import Sampler

np.set_printoptions(threshold=np.inf)

# Try to incorporate rdt
dn = DataNavigator('../demo/Airbnb_demo_meta.json')
dn.transform_data()
print('Data', dn.data)
print('child map', dn.child_map)
print('parent map', dn.parent_map)
print('transformed data', dn.transformed_data)

modeler = Modeler(dn)
modeler.model_database()
modeler.save_model('example2')
# modeler = load_model('models/example3.pkl')
print('customers table', modeler.models['users'].data)
print('orders table', modeler.models['sessions'].data)
sampler = Sampler(dn, modeler)
print('generated users', sampler.sample_rows('users', 2))
print('generated sessions', sampler.sample_rows('sessions', 10))
print('sampling everything', sampler.sample_all())
# print('sampling specific table', sampler.sample_table('users'))
