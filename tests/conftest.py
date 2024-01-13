"""This file contains the fixtures needed for the tests."""

import os

import pytest
from autonav.file_handlers import _readpathfile
from numpy import array, insert


@pytest.fixture(scope="session")
def default_values():
    """This fixture defines the default values to be used in the algorithm tests."""
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = ROOT_DIR + "/path_files/Path_small.txt"
    destinations = _readpathfile(filename)
    N = 8  # Number of anchors
    B = 200  # Area border in meters
    K = 50  # Number of measurement samples
    a_i = array(
        [
            [0, 0, 0],
            [0, B, 0],
            [B / 2, 0, 0],
            [B / 2, B, 0],
            [0, 0, B / 8],
            [0, B, B / 8],
            [B / 2, 0, B / 8],
            [B / 2, B, B / 8],
        ]
    ).T
    initial_uav_position = [10, 10, 5]
    return [a_i, N, K, destinations, initial_uav_position]


@pytest.fixture(scope="session")
def ideal_trajectory():
    """This fixture contains the ideal trajectory for the plots.py tests."""
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    filename = ROOT_DIR + "/path_files/Path_small.txt"
    ideal_trajectory = _readpathfile(filename)
    ideal_trajectory = insert(ideal_trajectory, 0, [10, 10, 5], axis=0)
    return ideal_trajectory


@pytest.fixture(scope="session")
def metrics_trajectories():
    """This fixture contains the trajectories for the metrics.py tests."""
    estimated_trajectory = array(
        [
            [9.99999962, 9.99999996, 4.99999754],
            [11.99410947, 9.84660779, 5.00000705],
            [13.98821739, 9.69321436, 5.00000066],
            [15.98232633, 9.53982188, 5.0000055],
            [17.97643436, 9.38642838, 4.99999871],
            [19.97054325, 9.23303628, 5.00000696],
            [21.96465149, 9.07964328, 5.00000546],
            [23.95875955, 8.92624995, 5.00000067],
            [25.95286755, 8.77285661, 4.9999958],
            [27.94697505, 8.61946163, 4.99997503],
            [29.94108338, 8.46607013, 4.99998826],
        ]
    )
    true_trajectory = array(
        [
            [10.0, 10.0, 5.0],
            [11.99410897, 9.846607, 5.00000008],
            [13.98821794, 9.69321398, 4.99999985],
            [15.98232691, 9.53982097, 4.99999983],
            [17.97643588, 9.38642795, 4.99999964],
            [19.97054485, 9.23303494, 4.99999969],
            [21.96465382, 9.0796419, 4.99999944],
            [23.95876279, 8.92624886, 4.99999923],
            [25.95287175, 8.77285584, 4.99999921],
            [27.94698072, 8.61946283, 4.99999938],
            [29.9410897, 8.46606991, 5.00000044],
        ]
    )
    return [estimated_trajectory, true_trajectory]


@pytest.fixture(scope="session")
def expected_trajectories_gtrs():
    """This fixture defines the expected GTRS trajectories for sigma = 0."""
    expected_estimated_trajectory = array(
        [
            [9.99999962, 9.99999996, 4.99999754],
            [11.99410947, 9.84660779, 5.00000705],
            [13.98821739, 9.69321436, 5.00000066],
            [15.98232633, 9.53982188, 5.0000055],
            [17.97643436, 9.38642838, 4.99999871],
            [19.97054325, 9.23303628, 5.00000696],
            [21.96465149, 9.07964328, 5.00000546],
            [23.95875955, 8.92624995, 5.00000067],
            [25.95286755, 8.77285661, 4.9999958],
            [27.94697505, 8.61946163, 4.99997503],
            [29.94108338, 8.46607013, 4.99998826],
            [31.93519126, 8.31267747, 4.99999003],
            [33.92929895, 8.15928452, 4.99998914],
            [35.92340664, 8.00589281, 4.99999963],
            [37.91751374, 7.85249744, 4.99997654],
            [39.9116211, 7.69910598, 4.9999893],
            [41.90572815, 7.5457138, 4.9999955],
            [43.89983488, 7.39231955, 4.99998327],
            [45.89394148, 7.23892688, 4.99998525],
            [47.88804782, 7.08553417, 4.99998713],
            [49.88215387, 6.93214165, 4.99999082],
            [51.87625965, 6.77874629, 4.99996981],
            [53.87036509, 6.62535413, 4.99997706],
            [55.86447021, 6.47196031, 4.99997007],
            [57.85857491, 6.31856718, 4.99996936],
            [59.85267913, 6.16517445, 4.99997222],
            [61.84678297, 6.01178011, 4.99996124],
            [63.840886, 5.858389, 4.9999783],
            [65.83498843, 5.70499653, 4.99998323],
            [67.82909036, 5.55160199, 4.99996971],
            [69.82319137, 5.39820917, 4.9999697],
            [71.81729124, 5.24481823, 4.9999832],
            [73.08723003, 5.14712919, 4.99996762],
            [73.54591463, 5.11184689, 4.9999744],
            [73.81098913, 5.09145874, 4.99999118],
            [73.98822888, 5.07782342, 4.99997626],
            [74.11656591, 5.06795347, 4.99999324],
            [74.46919408, 7.03661852, 4.99998351],
            [74.66894447, 8.1517932, 4.99999847],
            [74.74664366, 8.5855722, 4.99999806],
            [74.79215043, 8.83962841, 5.00000283],
            [74.82277761, 9.0106157, 5.00001079],
            [74.84504439, 9.13492198, 4.99999641],
            [74.87356498, 11.13471714, 4.99999037],
            [74.90208546, 13.13451276, 4.99998951],
            [74.93060606, 15.13430836, 4.99998812],
            [74.95912607, 17.13410477, 4.99999868],
            [74.97377036, 18.16087768, 4.99999037],
            [74.97980012, 18.5837176, 5.00000263],
            [74.98337668, 18.8344748, 4.99999919],
            [74.98579943, 19.00429746, 4.99998899],
            [74.99289167, 21.00001427, 4.99999286],
            [74.99466774, 21.50001083, 5.00000577],
            [74.9956666, 21.7812591, 5.00001546],
            [74.99632775, 21.96692558, 4.99999936],
            [74.99680194, 22.10033171, 4.99999915],
            [72.9988327, 22.19022398, 5.00000564],
            [71.00086184, 22.28011658, 5.00002381],
            [69.00289079, 22.3700082, 5.00003193],
            [67.00491894, 22.45989956, 5.00004141],
            [65.00694724, 22.54978924, 5.00003101],
            [63.00897432, 22.63967956, 5.00003585],
            [61.01100172, 22.72956735, 5.00000958],
            [59.01302789, 22.81945661, 5.00001108],
            [57.01505368, 22.90934483, 5.00000514],
            [56.50698593, 22.93220394, 5.00002534],
            [56.22282383, 22.94498698, 5.00000759],
            [56.03572281, 22.95340496, 5.00001401],
            [55.90149731, 22.95944332, 5.00000908],
            [53.90150535, 22.96332427, 5.00000495],
            [51.9015129, 22.96720617, 5.00001594],
            [49.9015202, 22.97108698, 5.00001291],
            [47.90152719, 22.97496818, 5.00001688],
            [45.9015338, 22.97884836, 5.00000755],
            [43.9015403, 22.98272962, 5.0000147],
            [41.90154672, 22.98661097, 5.00002434],
            [39.90155243, 22.99049038, 5.00000717],
            [37.9015584, 22.99437128, 5.00001256],
            [36.84917737, 22.99641308, 5.00001178],
            [36.42174465, 22.99724187, 5.00000419],
            [36.16907544, 22.99773346, 5.00002445],
            [35.99823242, 22.99806347, 5.00000277],
            [33.99823364, 22.99841505, 4.99999279],
            [31.99823594, 22.99876851, 5.00001216],
            [29.99823636, 22.99911947, 4.99999257],
            [27.99823743, 22.99947184, 4.9999955],
            [26.87456153, 22.99967149, 5.00002584],
            [26.43531346, 22.99974791, 5.00001031],
            [26.17779806, 22.99979318, 5.0000093],
            [26.00439712, 22.99982364, 5.00000802],
            [25.87829565, 22.99984591, 5.00000922],
            [23.87829635, 22.99987405, 5.00000446],
            [21.87829837, 22.99990305, 5.00001575],
            [19.87829775, 22.99993053, 4.99999766],
            [17.87829817, 22.99995894, 4.99999709],
            [16.84272206, 22.99997327, 4.99998799],
            [16.41827174, 22.9999803, 5.0000108],
            [16.16683478, 22.99998372, 5.00000745],
            [15.99664643, 22.99998595, 5.00000291],
            [13.9966477, 22.99999081, 5.00000694],
            [11.99999902, 22.99999535, 5.00000285],
            [11.5000011, 22.99999678, 5.00001039],
            [11.21874663, 22.99999662, 4.99998552],
            [11.03308203, 22.99999772, 5.00000578],
            [10.89967246, 22.99999761, 4.99999256],
            [10.83306671, 24.99888797, 4.99999069],
            [10.76646263, 26.99777852, 4.99999727],
            [10.69985761, 28.99666889, 4.99999882],
            [10.63325055, 30.995559, 4.99999039],
            [10.56664504, 32.99444925, 4.99998966],
            [10.50004, 34.99333949, 4.99999106],
            [10.43343417, 36.99222964, 4.99998899],
            [10.36682757, 38.99111969, 4.9999837],
            [10.30022363, 40.99000987, 4.99999026],
            [10.23362179, 42.9889001, 5.00000569],
            [10.16701067, 44.98778982, 4.99998245],
            [10.10040634, 46.98667981, 4.99998839],
            [10.06256885, 48.12232177, 5.00000395],
            [10.04787528, 48.56327566, 5.00000293],
            [10.03927281, 48.82144089, 5.00000314],
            [10.03348072, 48.99516226, 4.99998951],
        ]
    )
    expected_true_trajectory = array(
        [
            [10.0, 10.0, 5.0],
            [11.99410897, 9.846607, 5.00000008],
            [13.98821794, 9.69321398, 4.99999985],
            [15.98232691, 9.53982097, 4.99999983],
            [17.97643588, 9.38642795, 4.99999964],
            [19.97054485, 9.23303494, 4.99999969],
            [21.96465382, 9.0796419, 4.99999944],
            [23.95876279, 8.92624886, 4.99999923],
            [25.95287175, 8.77285584, 4.99999921],
            [27.94698072, 8.61946283, 4.99999938],
            [29.9410897, 8.46606991, 5.00000044],
            [31.93519867, 8.31267693, 5.00000095],
            [33.92930765, 8.15928394, 5.00000142],
            [35.92341662, 8.00589095, 5.00000194],
            [37.91752558, 7.8524979, 5.00000196],
            [39.91163456, 7.69910498, 5.00000322],
            [41.90574353, 7.54571199, 5.00000383],
            [43.8998525, 7.39231895, 5.0000041],
            [45.89396148, 7.23892601, 5.00000518],
            [47.88807045, 7.08553306, 5.00000619],
            [49.88217942, 6.93214011, 5.00000713],
            [51.8762884, 6.77874714, 5.00000786],
            [53.87039739, 6.62535439, 5.00001047],
            [55.86450638, 6.47196162, 5.00001263],
            [57.85861538, 6.31856899, 5.00001575],
            [59.85272438, 6.16517645, 5.00001931],
            [61.84683339, 6.01178399, 5.00002297],
            [63.84094243, 5.85839187, 5.00002885],
            [65.83505146, 5.70499965, 5.00003272],
            [67.82916051, 5.55160759, 5.00003637],
            [69.82326962, 5.39821638, 5.00004479],
            [71.81737879, 5.24482601, 5.00005647],
            [73.08732364, 5.14714015, 5.00006317],
            [73.5460107, 5.1118582, 5.00007093],
            [73.81108694, 5.09146878, 5.0000756],
            [73.98832732, 5.07783545, 5.00007692],
            [74.11666539, 5.06796394, 5.00007993],
            [74.46929549, 7.03663151, 5.00008263],
            [74.66904742, 8.15180589, 5.00008883],
            [74.74674708, 8.58558522, 5.00008919],
            [74.7922543, 8.83964114, 5.00008954],
            [74.82288197, 9.01062769, 5.00008912],
            [74.84514844, 9.13493534, 5.00008777],
            [74.87366915, 11.13473197, 5.00008843],
            [74.90218988, 13.1345286, 5.0000906],
            [74.93071067, 15.13432523, 5.00009366],
            [74.95923155, 17.13412186, 5.00009854],
            [74.97387559, 18.16089571, 5.00009901],
            [74.97990614, 18.58373507, 5.00010123],
            [74.98348259, 18.83449255, 5.00010076],
            [74.9859047, 19.00431594, 5.00010088],
            [74.9929974, 21.0000334, 5.00010638],
            [74.99477449, 21.50002942, 5.00010816],
            [74.99577428, 21.78127714, 5.00010708],
            [74.99643445, 21.96694448, 5.00010473],
            [74.99690867, 22.10035067, 5.00010481],
            [72.99892975, 22.19024096, 5.00010489],
            [71.00095083, 22.28013098, 5.00010427],
            [69.00297189, 22.37002063, 5.00010129],
            [67.00499293, 22.45990995, 5.00009674],
            [65.00701396, 22.54979888, 5.00008985],
            [63.00903497, 22.6396876, 5.00008365],
            [61.01105597, 22.72957584, 5.00007471],
            [59.01307697, 22.81946415, 5.00007153],
            [57.01509794, 22.90935187, 5.00006601],
            [56.50702938, 22.93220934, 5.00006471],
            [56.22286643, 22.94499322, 5.00005993],
            [56.03576511, 22.95341063, 5.00005877],
            [55.90153927, 22.95944918, 5.00005696],
            [53.90154304, 22.96332991, 5.00005609],
            [51.9015468, 22.96721063, 5.00005556],
            [49.90155057, 22.9710912, 5.00005368],
            [47.90155433, 22.97497174, 5.00005194],
            [45.90155809, 22.97885217, 5.00004933],
            [43.90156186, 22.98273266, 5.00004794],
            [41.90156562, 22.98661296, 5.00004464],
            [39.90156939, 22.99049296, 5.00003758],
            [37.90157315, 22.9943732, 5.00003466],
            [36.84919103, 22.99641472, 5.0000301],
            [36.42175811, 22.99724383, 5.00002738],
            [36.1690879, 22.997734, 5.00002664],
            [35.99824541, 22.99806522, 5.00002306],
            [33.99824544, 22.99841737, 5.00002256],
            [31.99824547, 22.99876965, 5.00002416],
            [29.9982455, 22.99912159, 5.00002069],
            [27.99824553, 22.99947393, 5.00002366],
            [26.87456705, 22.99967187, 5.00002535],
            [26.43531943, 22.99974885, 5.00001929],
            [26.17780384, 22.99979408, 5.00001744],
            [26.0044028, 22.99982453, 5.00001607],
            [25.8783011, 22.99984667, 5.00001506],
            [23.8783011, 22.999875, 5.00001337],
            [21.8783011, 22.99990337, 5.00001237],
            [19.8783011, 22.99993156, 5.00000779],
            [17.8783011, 22.99996004, 5.00000875],
            [16.84272606, 22.99997481, 5.00000979],
            [16.41827299, 22.99998097, 5.00001256],
            [16.16683614, 22.99998446, 5.00001064],
            [15.99664822, 22.99998684, 5.00000956],
            [13.99664822, 22.99999152, 5.00000859],
            [11.99999911, 22.99999611, 5.00000512],
            [11.4999996, 22.99999728, 5.0000044],
            [11.21874919, 22.99999788, 5.00000245],
            [11.03308127, 22.9999984, 5.00000466],
            [10.89967396, 22.99999869, 5.00000391],
            [10.83306852, 24.99888931, 5.00000446],
            [10.76646312, 26.99777993, 5.00000521],
            [10.6998576, 28.99667055, 5.00000545],
            [10.63325203, 30.99556117, 5.00000556],
            [10.56664662, 32.99445179, 5.00000657],
            [10.50004122, 34.99334241, 5.00000779],
            [10.43343578, 36.99223304, 5.00000898],
            [10.3668304, 38.99112366, 5.00001067],
            [10.30022524, 40.99001429, 5.00001363],
            [10.23361982, 42.98890491, 5.00001579],
            [10.16701338, 44.9877955, 5.00001417],
            [10.10040881, 46.98668615, 5.00002117],
            [10.06256827, 48.12232838, 5.00002554],
            [10.0478746, 48.56328243, 5.00002461],
            [10.03927188, 48.82144775, 5.00002409],
            [10.033483, 48.99516932, 5.00002363],
        ]
    )
    return [expected_estimated_trajectory, expected_true_trajectory]


@pytest.fixture(scope="session")
def expected_trajectories_wls():
    """This fixture defines the expected WLS trajectories for sigma = 0."""
    expected_estimated_trajectory = array(
        [
            [9.9999993, 10.00000109, 4.99999943],
            [11.99410737, 9.84660832, 5.00000026],
            [13.98821967, 9.69320963, 5.0000001],
            [15.98232553, 9.5398237, 4.99999836],
            [17.97643382, 9.38643074, 4.99999968],
            [19.97054326, 9.23303459, 4.99999956],
            [21.9646521, 9.07964506, 5.0000014],
            [23.95876099, 8.92624908, 4.99999957],
            [25.95287373, 8.77285377, 5.00000177],
            [27.94698079, 8.61946441, 4.99999932],
            [29.9410906, 8.46607191, 4.99999841],
            [31.93519986, 8.31266806, 4.9999981],
            [33.92930824, 8.15928434, 5.00000072],
            [35.92341455, 8.00589278, 4.99999881],
            [37.9175268, 7.85249361, 5.00000262],
            [39.91163534, 7.69910717, 5.00000394],
            [41.90574261, 7.54571382, 4.99999521],
            [43.89985363, 7.39232028, 5.00000125],
            [45.89396392, 7.23892505, 4.99999995],
            [47.88807088, 7.08553094, 5.00000089],
            [49.88217939, 6.93213604, 5.0000017],
            [51.87628775, 6.77874597, 5.00000322],
            [53.87039765, 6.62536051, 5.00000376],
            [55.86450699, 6.47196277, 4.99999727],
            [57.85861581, 6.31857072, 4.99999953],
            [59.85272479, 6.16517489, 5.00000141],
            [61.84683255, 6.011784, 4.99999849],
            [63.840942, 5.85838746, 4.9999952],
            [65.83505156, 5.70499024, 5.00000168],
            [67.82916038, 5.55160715, 5.00000364],
            [69.82326883, 5.39820926, 5.00000061],
            [71.81737836, 5.24481779, 4.99999769],
            [73.08725323, 5.1471274, 5.00000102],
            [73.54592783, 5.11184772, 4.99999896],
            [73.81100068, 5.09146225, 4.99999953],
            [73.98823774, 5.07783282, 4.99999931],
            [74.11657462, 5.06795795, 4.99999923],
            [74.46919856, 7.0366213, 5.00000053],
            [74.66895307, 8.15180161, 5.00000116],
            [74.74664887, 8.58557321, 4.99999871],
            [74.7921523, 8.83962118, 5.00000116],
            [74.82278151, 9.01061636, 4.99999962],
            [74.84504831, 9.13492322, 5.00000043],
            [74.87356775, 11.13471957, 4.99999918],
            [74.90208982, 13.13451781, 5.00000181],
            [74.93060747, 15.13431189, 4.99999676],
            [74.95912756, 17.13411298, 5.00000298],
            [74.97377337, 18.16088161, 4.99999679],
            [74.97980204, 18.58371732, 5.00000427],
            [74.98337573, 18.83447315, 5.00000047],
            [74.98579921, 19.00429541, 4.99999716],
            [74.99289411, 21.00002041, 5.00000378],
            [74.99466704, 21.50000909, 5.0000014],
            [74.9956711, 21.78125763, 4.99999718],
            [74.99633065, 21.96692738, 5.00000067],
            [74.99680316, 22.100334, 5.00000146],
            [72.99882332, 22.19022077, 4.99999944],
            [71.00084418, 22.2801133, 4.99999796],
            [69.00286548, 22.36999988, 4.99999445],
            [67.00488896, 22.4598915, 4.99999858],
            [65.00690679, 22.54978343, 5.00000481],
            [63.00892849, 22.63967282, 5.00000018],
            [61.01095089, 22.72956853, 4.99999725],
            [59.01297148, 22.8194517, 5.00000052],
            [57.01499338, 22.90934436, 5.00000593],
            [56.50695378, 22.93220145, 4.99999808],
            [56.22280291, 22.94498356, 4.99999965],
            [56.03570878, 22.95340033, 4.99999273],
            [55.90148512, 22.95944439, 4.99999855],
            [53.90148845, 22.96332133, 5.00000546],
            [51.90149337, 22.96720082, 4.9999969],
            [49.90149489, 22.97108389, 4.9999992],
            [47.9014999, 22.97496387, 5.00000036],
            [45.90150606, 22.97884676, 4.99999757],
            [43.90150838, 22.98273248, 5.00000602],
            [41.90151382, 22.98660318, 4.99999791],
            [39.90151561, 22.99048946, 5.0000006],
            [37.90151907, 22.99437042, 4.99999839],
            [36.84916721, 22.99641192, 5.00000188],
            [36.42173916, 22.99723998, 5.00000176],
            [36.16906782, 22.99773332, 4.99999836],
            [35.99823097, 22.99806255, 5.00000266],
            [33.99822799, 22.99841107, 4.99999533],
            [31.99822875, 22.99876461, 4.99999803],
            [29.99822716, 22.99912335, 5.00000105],
            [27.99822923, 22.9994715, 5.00000092],
            [26.87455734, 22.99967185, 5.00000551],
            [26.43530897, 22.99974967, 5.00000045],
            [26.17779958, 22.9997874, 4.99999764],
            [26.00439601, 22.99982579, 5.00000032],
            [25.87829325, 22.99984809, 4.99999776],
            [23.87829228, 22.99987518, 4.99999887],
            [21.8782932, 22.99990139, 4.99999841],
            [19.87829116, 22.99993049, 5.0000008],
            [17.878293, 22.99996157, 5.00000068],
            [16.84272205, 22.99997267, 4.9999995],
            [16.41826841, 22.99998017, 4.99999935],
            [16.16683176, 22.99998497, 5.00000066],
            [15.99664721, 22.99998529, 5.00000079],
            [13.99664961, 22.99998886, 5.0000021],
            [11.99999562, 22.99999507, 4.99999908],
            [11.49999717, 22.99999675, 4.99999918],
            [11.21874889, 22.99999622, 4.99999674],
            [11.03308001, 22.99999881, 4.99999958],
            [10.89967361, 22.99999976, 5.00000068],
            [10.83306658, 24.99888828, 4.99999807],
            [10.76646303, 26.99777778, 4.9999981],
            [10.69985544, 28.99667157, 5.00000229],
            [10.63325231, 30.99556035, 5.00000258],
            [10.56665131, 32.9944501, 5.00000156],
            [10.50003977, 34.99334071, 4.99999848],
            [10.43343671, 36.99223039, 5.00000194],
            [10.3668267, 38.99112273, 4.99999766],
            [10.30022817, 40.99001322, 5.00000223],
            [10.23362095, 42.98890152, 4.99999564],
            [10.16701151, 44.98779424, 4.99999428],
            [10.10040943, 46.98668598, 5.00000648],
            [10.06256659, 48.12232144, 4.99999687],
            [10.04787145, 48.56327827, 4.99999838],
            [10.03927277, 48.82143936, 4.9999978],
            [10.03347663, 48.99516167, 4.99999737],
        ]
    )
    expected_true_trajectory = array(
        [
            [10.0, 10.0, 5.0],
            [11.99410897, 9.84660697, 5.00000002],
            [13.98821794, 9.69321394, 5.00000001],
            [15.98232692, 9.53982108, 5.00000001],
            [17.97643588, 9.38642799, 5.00000006],
            [19.97054485, 9.2330349, 5.00000007],
            [21.96465382, 9.07964193, 5.00000009],
            [23.95876278, 8.92624882, 5.00000004],
            [25.95287175, 8.77285582, 5.00000005],
            [27.94698073, 8.61946291, 4.99999998],
            [29.9410897, 8.46606985, 5.00000001],
            [31.93519866, 8.31267677, 5.00000008],
            [33.92930766, 8.15928418, 5.00000017],
            [35.92341663, 8.00589117, 5.00000013],
            [37.9175256, 7.85249809, 5.00000019],
            [39.91163459, 7.69910532, 5.00000005],
            [41.90574355, 7.5457122, 4.99999983],
            [43.89985251, 7.3923191, 5.00000012],
            [45.89396148, 7.23892602, 5.00000004],
            [47.88807045, 7.08553307, 5.00000004],
            [49.88217943, 6.93214023, 4.99999998],
            [51.87628843, 6.77874754, 4.99999984],
            [53.87039741, 6.62535464, 4.99999956],
            [55.86450633, 6.47196104, 4.99999921],
            [57.85861529, 6.31856786, 4.99999949],
            [59.85272424, 6.16517455, 4.99999955],
            [61.84683321, 6.01178156, 4.99999936],
            [63.84094216, 5.85838828, 4.99999959],
            [65.83505115, 5.70499557, 5.00000045],
            [67.82916022, 5.55160383, 5.00000008],
            [69.8232691, 5.39820969, 4.99999907],
            [71.8173781, 5.24481701, 4.99999884],
            [73.08725362, 5.14713399, 4.99999976],
            [73.54592955, 5.11185289, 4.99999951],
            [73.811001, 5.09146351, 4.9999997],
            [73.98823799, 5.07782978, 4.99999977],
            [74.11657391, 5.06795716, 4.99999986],
            [74.46920095, 7.03662528, 5.00000017],
            [74.66895095, 8.1517973, 4.99999997],
            [74.74664819, 8.58557239, 4.9999997],
            [74.79215441, 8.83962779, 4.99999993],
            [74.82278199, 9.01061639, 4.99999976],
            [74.84504794, 9.13492379, 4.9999998],
            [74.87356793, 11.13472043, 4.99999973],
            [74.90208804, 13.13451708, 4.99999991],
            [74.93060759, 15.13431372, 4.99999939],
            [74.9591279, 17.13411036, 5.00000072],
            [74.97377137, 18.16087832, 4.99999965],
            [74.97980122, 18.58371586, 5.00000039],
            [74.98337733, 18.83447343, 4.99999963],
            [74.98579958, 19.00429731, 4.99999956],
            [74.9928924, 21.00001681, 5.00000098],
            [74.99466886, 21.50000976, 5.00000004],
            [74.99566879, 21.78125813, 4.99999977],
            [74.99632828, 21.96692592, 5.0000002],
            [74.99680212, 22.10033164, 5.00000012],
            [72.99882319, 22.1902217, 4.99999997],
            [71.00084429, 22.28011212, 5.00000003],
            [69.00286537, 22.37000228, 5.00000029],
            [67.00488647, 22.45989295, 5.00000108],
            [65.00690757, 22.54978344, 5.00000132],
            [63.00892865, 22.63967368, 5.00000036],
            [61.01094975, 22.72956412, 5.00000031],
            [59.01297076, 22.81945279, 5.00000123],
            [57.0149919, 22.90934421, 5.00000097],
            [56.50695371, 22.93220112, 4.99999947],
            [56.22280286, 22.9449852, 4.99999984],
            [56.03570791, 22.95340299, 4.99999989],
            [55.90148567, 22.95944205, 5.00000083],
            [53.90148944, 22.96332269, 5.00000097],
            [51.9014932, 22.96720372, 5.00000039],
            [49.90149697, 22.97108493, 5.00000076],
            [47.90150073, 22.97496589, 5.00000087],
            [45.9015045, 22.978847, 5.00000081],
            [43.90150826, 22.98272778, 5.00000126],
            [41.90151203, 22.98660746, 4.99999991],
            [39.9015158, 22.99048974, 5.00000051],
            [37.90151956, 22.99437038, 5.00000027],
            [36.84916596, 22.99641218, 5.00000085],
            [36.42173774, 22.99724155, 5.00000042],
            [36.16906948, 22.99773205, 5.0000001],
            [35.99822921, 22.99806329, 5.00000034],
            [33.99822924, 22.99841561, 4.99999986],
            [31.99822928, 22.99876878, 5.0000009],
            [29.99822931, 22.99912183, 5.00000146],
            [27.99822934, 22.99947262, 5.00000104],
            [26.87455701, 22.99967069, 5.00000069],
            [26.43531135, 22.99974758, 4.9999994],
            [26.17779737, 22.9997925, 4.99999932],
            [26.00439588, 22.9998238, 4.99999967],
            [25.87829446, 22.99984567, 4.99999963],
            [23.87829446, 22.9998736, 5.00000004],
            [21.87829446, 22.99990171, 5.0000003],
            [19.87829446, 22.99993038, 5.00000076],
            [17.87829446, 22.99995888, 5.00000043],
            [16.84272314, 22.99997271, 5.00000018],
            [16.41827007, 22.999979, 5.0000003],
            [16.16683441, 22.99998252, 5.00000041],
            [15.99664736, 22.99998471, 5.00000032],
            [13.99664736, 22.99998962, 5.00000005],
            [11.99999635, 22.99999518, 4.999999],
            [11.49999854, 22.99999642, 4.99999923],
            [11.2187496, 22.99999703, 4.99999939],
            [11.03308099, 22.9999976, 4.99999988],
            [10.8996742, 22.99999775, 4.99999994],
            [10.83306868, 24.99888837, 4.99999989],
            [10.76646328, 26.997779, 5.00000004],
            [10.69985773, 28.99666961, 5.00000021],
            [10.63325236, 30.99556024, 4.99999999],
            [10.56664676, 32.99445085, 4.99999972],
            [10.50004062, 34.99334145, 4.99999953],
            [10.4334352, 36.99223207, 4.99999974],
            [10.36682943, 38.99112268, 4.99999944],
            [10.30022441, 40.99001332, 4.99999987],
            [10.23361796, 42.9889039, 4.99999937],
            [10.16701174, 44.9877945, 5.00000061],
            [10.10040679, 46.98668514, 5.0000029],
            [10.06256516, 48.12232276, 5.00000045],
            [10.04787201, 48.56327695, 5.00000119],
            [10.03927, 48.82144131, 5.00000148],
            [10.03348112, 48.99516333, 5.0000018],
        ]
    )
    return [expected_estimated_trajectory, expected_true_trajectory]
