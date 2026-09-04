class Lab:
  def __init__ (self, room_number)
  self.room_number = room_number

class Technician:
  def __init__ (self, name)
  self.name = name
  self.assigned_lab = none

def assign_lab(self, lab_obj):
  self.assigned_lab = lab_obj

chem_lab = Lab("302")
mr_cruz = technician("mr. Cruz")

mr_cruz.assign_lab(chem_lab)

print(mr_cruz.assigned.lab.room_number)
