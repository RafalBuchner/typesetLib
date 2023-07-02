import unittest
import os
import pprint
import sys


article = open("article.txt", "r").read()


class AbstractObjectsTest(unittest.TestCase):
    def test_text(self):
        from typesetLib.abstract.text import AbstractText
        txt = AbstractText()
        # self.assertIsNotNone(ruleConditionDesc)

        # self.assertIsNone(ruleConditionDesc.name)
        # ruleConditionDesc.setName("Optical Size")
        # self.assertIsNotNone(ruleConditionDesc.name)

        # with self.assertRaises(AssertionError) as context:
        #     ruleConditionDesc.setName(2.3)

        # self.assertIsNone(ruleConditionDesc.minimum)
        # ruleConditionDesc.setMinimum(8)
        # self.assertIsNotNone(ruleConditionDesc.minimum)

        # with self.assertRaises(AssertionError) as context:
        #     ruleConditionDesc.setMinimum("Optical Size")

        # self.assertIsNone(ruleConditionDesc.maximum)
        # ruleConditionDesc.setMaximum(28)
        # self.assertIsNotNone(ruleConditionDesc.maximum)

        # with self.assertRaises(AssertionError) as context:
        #     ruleConditionDesc.setMaximum("Optical Size")

        # ruleEntryDesc = RuleEntryDescriptor()
        # self.assertIsNotNone(ruleConditionDesc)

        # self.assertIsNone(ruleEntryDesc.glyphSuffix)
        # ruleEntryDesc.setGlyphSuffix(".rule")
        # self.assertIsNotNone(ruleEntryDesc.glyphSuffix)

        # with self.assertRaises(AssertionError) as context:
        #     ruleEntryDesc.setGlyphSuffix(3213)

        # self.assertIsNone(ruleEntryDesc.ruleName)
        # ruleEntryDesc.setRuleName("opsz_alt")
        # self.assertIsNotNone(ruleEntryDesc.ruleName)

        # with self.assertRaises(AssertionError) as context:
        #     ruleEntryDesc.setRuleName(dict())

        # self.assertIsInstance(ruleEntryDesc.conditionSet, list)
        # self.assertEqual(
        #         len(ruleEntryDesc.conditionSet), 0
        #     )
        # ruleEntryDesc.setConditionSet([ruleConditionDesc])
        # self.assertNotEqual(len(list(ruleEntryDesc.conditionSet)), 0)

        # with self.assertRaises(AssertionError) as context:
        #     ruleEntryDesc.setConditionSet(["lala"])

        # with self.assertRaises(AssertionError) as context:
        #     ruleEntryDesc.setConditionSet({"lala":23})

        # ruleEntryDesc.setConditionSet([])
        # self.assertEqual(
        #         len(ruleEntryDesc.conditionSet), 0
        #     )
        # ruleEntryDesc.addRuleCondition(ruleConditionDesc)
        # self.assertNotEqual(len(list(ruleEntryDesc.conditionSet)), 0)

        # with self.assertRaises(AssertionError) as context:
        #     ruleEntryDesc.addRuleCondition(111111)


        # rulesDesc = RulesDescriptor()
        # self.assertIsNotNone(rulesDesc)


        # self.assertEqual(len(rulesDesc.rules.keys()), 0)
        # rulesDesc.setRules({ruleEntryDesc.ruleName:ruleEntryDesc})
        # self.assertNotEqual(len(list(rulesDesc.rules.keys())), 0)
        
        # rulesDesc.setRules({})
        # self.assertEqual(len(list(rulesDesc.rules.keys())), 0)

        

if __name__ == "__main__":
    
    unittest.main()
