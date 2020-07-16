import unittest


from stchger.setting_io import read_setting


class TestReadSetting(unittest.TestCase):
    def setUp(self):
        self.datas = read_setting("tests/test_data.xlsx")
        self.glasses_desks_ans = set(
            [(3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3)]
        )

    def test_member_keys(self):
        key = self.datas["member_keys"]
        self.assertIn("number", key)
        self.assertIn("name", key)

    def test_desks_map(self):
        name_coord, coord_name = self.datas["desks_map"]
        self.assertEqual(name_coord["A2"], (1, 2))
        self.assertEqual(name_coord["D5"], (4, 5))
        self.assertEqual(name_coord["E7"], (5, 7))
        self.assertEqual(coord_name[(3, 4)], "C4")
        self.assertEqual(coord_name[(3, 7)], "C7")
        self.assertEqual(coord_name[(6, 1)], "F1")

    def test_seat_places(self):
        seat_places = set(self.datas["seat_places"])
        ans = set([(i, j) for i in range(1, 8) for j in range(1, 8)]) - set(
            [(1, 1), (7, 1)]
        )
        self.assertEqual(seat_places, ans)

    def test_glasses_desks(self):
        glasses_desks = set(self.datas["glasses_desks"])
        self.assertEqual(glasses_desks, self.glasses_desks_ans)

    def test_members(self):
        members = self.datas["members"]
        for i, m in enumerate(members, start=1):
            num = m["number"]
            name = m["name"]
            hopes = m["hopes"]
            glass = m["glasses"]
            self.assertEqual(i, num)
            if i == 1:
                self.assertEqual(name, "川野 洵子")
                self.assertEqual(hopes, ((1, 2),))
                self.assertEqual(glass, ())
            if i == 39:
                self.assertEqual(name, "工藤 宏幸")
                self.assertEqual(hopes, ((3, 1), (3, 2), (3, 3)))
                self.assertEqual(set(glass), self.glasses_desks_ans)
