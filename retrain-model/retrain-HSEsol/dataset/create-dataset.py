from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifWriter

def electronic_bandGap(file_name):
    """
    This functions uses DOSCAR file generated in VASP simulations and returns the Fermi energy
    the band gap, and the energies of the band gap (respect the exchange-correlation functional
    used).

    file_name: path of the DOSCAR file
    """
    
    file = open(file_name, "r")

    for x in range(6):
        actual_string = file.readline()
        if x == 5:
            fermiEnergy = float(actual_string.split()[3])

    file.close()

    file = open(file_name, "r")

    for x in range(6):
        file.readline()

    for x in file:
        actual_string = x

        if (float(actual_string.split()[0]) <= fermiEnergy+0.1) and (float(actual_string.split()[0]) >= fermiEnergy-0.1):
            density_bandGap = float(actual_string.split()[2])

            break

    file.close()

    file = open(file_name, "r")

    for x in range(6):
        file.readline()

    for x in file:
        actual_string = x

        if float(actual_string.split()[2]) == density_bandGap:
            minEnergy = float(actual_string.split()[0])

            break   

    for x in file:
        actual_string = x

        if float(actual_string.split()[2]) != density_bandGap:
            maxEnergy = float(actual_string.split()[0])

            break 
    bandGap = maxEnergy - minEnergy

    file.close()
    
    return fermiEnergy, minEnergy, maxEnergy, bandGap

materials = open('materials.txt', 'w')
materials.write('material id       band gap (eV)\n')

# database 1
# pure compouds
for num in range(100):
    try:
        path_directory = '/home/pol/work/db-cap-ml-backup/db-HSEsol1/pure-compounds/struc-' + str(num+1).zfill(4)

        _, _, _, bandgap = electronic_bandGap(path_directory + '/DOSCAR')


        if bandgap > 0.1:
            structure = Poscar.from_file(path_directory + '/POSCAR').structure

            cif_writer = CifWriter(structure)
            cif_filename = 'CAP-structures/hsesol_1_pc_' + str(num+1).zfill(4) + '.cif'
            cif_writer.write_file(cif_filename)


            materials.write(f'hsesol_1_pc_{str(num+1).zfill(4)}       {bandgap}\n')

            print(f'Phase generated {num+1} of a total of 100')
        else:
            print(f'Phase {num+1} not accepted, no bandgap')
    except:
        print(f'Phase {num+1} jumped :(')

# solid solutions
for num in range(500):
    try:
        path_directory = '/home/pol/work/db-cap-ml-backup/db-HSEsol1/solid-solutions/struc-' + str(num+1).zfill(4)

        _, _, _, bandgap = electronic_bandGap(path_directory + '/DOSCAR')

        if bandgap > 0.1:
            structure = Poscar.from_file(path_directory + '/POSCAR').structure

            cif_writer = CifWriter(structure)
            cif_filename = 'CAP-structures/hsesol_1_ss_' + str(num+1).zfill(4) + '.cif'
            cif_writer.write_file(cif_filename)


            materials.write(f'hsesol_1_ss_{str(num+1).zfill(4)}       {bandgap}\n')

            print(f'Phase generated {num+1} of a total of 500')
        else:
            print(f'Phase {num+1} not accepted, no bandgap')
    except:
        print(f'Phase {num+1} jumped :(')

# database 2
# pure compouds
for num in range(150):
    try:
        path_directory = '/home/pol/work/db-cap-ml-backup/db-HSEsol2/pure-compounds/struc-' + str(num+1).zfill(4)

        _, _, _, bandgap = electronic_bandGap(path_directory + '/DOSCAR')


        if bandgap > 0.1:
            structure = Poscar.from_file(path_directory + '/POSCAR').structure

            cif_writer = CifWriter(structure)
            cif_filename = 'CAP-structures/hsesol_2_pc_' + str(num+1).zfill(4) + '.cif'
            cif_writer.write_file(cif_filename)


            materials.write(f'hsesol_2_pc_{str(num+1).zfill(4)}       {bandgap}\n')

            print(f'Phase generated {num+1} of a total of 150')
        else:
            print(f'Phase {num+1} not accepted, no bandgap')
    except:
        print(f'Phase {num+1} jumped :(')

# solid solutions
for num in range(250):
    try:
        path_directory = '/home/pol/work/db-cap-ml-backup/db-HSEsol2/solid-solutions/struc-' + str(num+1).zfill(4)

        _, _, _, bandgap = electronic_bandGap(path_directory + '/DOSCAR')

        if bandgap > 0.1:
            structure = Poscar.from_file(path_directory + '/POSCAR').structure

            cif_writer = CifWriter(structure)
            cif_filename = 'CAP-structures/hsesol_2_ss_' + str(num+1).zfill(4) + '.cif'
            cif_writer.write_file(cif_filename)


            materials.write(f'hsesol_2_ss_{str(num+1).zfill(4)}       {bandgap}\n')

            print(f'Phase generated {num+1} of a total of 250')
        else:
            print(f'Phase {num+1} not accepted, no bandgap')
    except:
        print(f'Phase {num+1} jumped :(')

materials.close()
