# Generated from SimpleC.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleCParser import SimpleCParser
else:
    from SimpleCParser import SimpleCParser

# This class defines a complete listener for a parse tree produced by SimpleCParser.
class SimpleCListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:SimpleCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:SimpleCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#postfixExpression.
    def enterPostfixExpression(self, ctx:SimpleCParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#postfixExpression.
    def exitPostfixExpression(self, ctx:SimpleCParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:SimpleCParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:SimpleCParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:SimpleCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:SimpleCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#unaryOperator.
    def enterUnaryOperator(self, ctx:SimpleCParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#unaryOperator.
    def exitUnaryOperator(self, ctx:SimpleCParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#castExpression.
    def enterCastExpression(self, ctx:SimpleCParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#castExpression.
    def exitCastExpression(self, ctx:SimpleCParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SimpleCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SimpleCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:SimpleCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:SimpleCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#shiftExpression.
    def enterShiftExpression(self, ctx:SimpleCParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#shiftExpression.
    def exitShiftExpression(self, ctx:SimpleCParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:SimpleCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:SimpleCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:SimpleCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:SimpleCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#andExpression.
    def enterAndExpression(self, ctx:SimpleCParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#andExpression.
    def exitAndExpression(self, ctx:SimpleCParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:SimpleCParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:SimpleCParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:SimpleCParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:SimpleCParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:SimpleCParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:SimpleCParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:SimpleCParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:SimpleCParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:SimpleCParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:SimpleCParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:SimpleCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:SimpleCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:SimpleCParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:SimpleCParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#expression.
    def enterExpression(self, ctx:SimpleCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#expression.
    def exitExpression(self, ctx:SimpleCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#constantExpression.
    def enterConstantExpression(self, ctx:SimpleCParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#constantExpression.
    def exitConstantExpression(self, ctx:SimpleCParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declaration.
    def enterDeclaration(self, ctx:SimpleCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declaration.
    def exitDeclaration(self, ctx:SimpleCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:SimpleCParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:SimpleCParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:SimpleCParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by SimpleCParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:SimpleCParser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by SimpleCParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:SimpleCParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:SimpleCParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:SimpleCParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:SimpleCParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#initDeclarator.
    def enterInitDeclarator(self, ctx:SimpleCParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#initDeclarator.
    def exitInitDeclarator(self, ctx:SimpleCParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:SimpleCParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:SimpleCParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:SimpleCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:SimpleCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:SimpleCParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:SimpleCParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#structOrUnion.
    def enterStructOrUnion(self, ctx:SimpleCParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#structOrUnion.
    def exitStructOrUnion(self, ctx:SimpleCParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:SimpleCParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:SimpleCParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#structDeclaration.
    def enterStructDeclaration(self, ctx:SimpleCParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleCParser#structDeclaration.
    def exitStructDeclaration(self, ctx:SimpleCParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleCParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:SimpleCParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:SimpleCParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:SimpleCParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:SimpleCParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#structDeclarator.
    def enterStructDeclarator(self, ctx:SimpleCParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#structDeclarator.
    def exitStructDeclarator(self, ctx:SimpleCParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:SimpleCParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:SimpleCParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#enumeratorList.
    def enterEnumeratorList(self, ctx:SimpleCParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#enumeratorList.
    def exitEnumeratorList(self, ctx:SimpleCParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#enumerator.
    def enterEnumerator(self, ctx:SimpleCParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#enumerator.
    def exitEnumerator(self, ctx:SimpleCParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:SimpleCParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by SimpleCParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:SimpleCParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by SimpleCParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:SimpleCParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:SimpleCParser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#typeQualifier.
    def enterTypeQualifier(self, ctx:SimpleCParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#typeQualifier.
    def exitTypeQualifier(self, ctx:SimpleCParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:SimpleCParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:SimpleCParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declarator.
    def enterDeclarator(self, ctx:SimpleCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declarator.
    def exitDeclarator(self, ctx:SimpleCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:SimpleCParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:SimpleCParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#gccDeclaratorExtension.
    def enterGccDeclaratorExtension(self, ctx:SimpleCParser.GccDeclaratorExtensionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#gccDeclaratorExtension.
    def exitGccDeclaratorExtension(self, ctx:SimpleCParser.GccDeclaratorExtensionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#gccAttributeSpecifier.
    def enterGccAttributeSpecifier(self, ctx:SimpleCParser.GccAttributeSpecifierContext):
        pass

    # Exit a parse tree produced by SimpleCParser#gccAttributeSpecifier.
    def exitGccAttributeSpecifier(self, ctx:SimpleCParser.GccAttributeSpecifierContext):
        pass


    # Enter a parse tree produced by SimpleCParser#gccAttributeList.
    def enterGccAttributeList(self, ctx:SimpleCParser.GccAttributeListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#gccAttributeList.
    def exitGccAttributeList(self, ctx:SimpleCParser.GccAttributeListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#gccAttribute.
    def enterGccAttribute(self, ctx:SimpleCParser.GccAttributeContext):
        pass

    # Exit a parse tree produced by SimpleCParser#gccAttribute.
    def exitGccAttribute(self, ctx:SimpleCParser.GccAttributeContext):
        pass


    # Enter a parse tree produced by SimpleCParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:SimpleCParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by SimpleCParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:SimpleCParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by SimpleCParser#pointer.
    def enterPointer(self, ctx:SimpleCParser.PointerContext):
        pass

    # Exit a parse tree produced by SimpleCParser#pointer.
    def exitPointer(self, ctx:SimpleCParser.PointerContext):
        pass


    # Enter a parse tree produced by SimpleCParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:SimpleCParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:SimpleCParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:SimpleCParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:SimpleCParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#parameterList.
    def enterParameterList(self, ctx:SimpleCParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#parameterList.
    def exitParameterList(self, ctx:SimpleCParser.ParameterListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:SimpleCParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleCParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:SimpleCParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleCParser#identifierList.
    def enterIdentifierList(self, ctx:SimpleCParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#identifierList.
    def exitIdentifierList(self, ctx:SimpleCParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#typeName.
    def enterTypeName(self, ctx:SimpleCParser.TypeNameContext):
        pass

    # Exit a parse tree produced by SimpleCParser#typeName.
    def exitTypeName(self, ctx:SimpleCParser.TypeNameContext):
        pass


    # Enter a parse tree produced by SimpleCParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:SimpleCParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:SimpleCParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:SimpleCParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:SimpleCParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#typedefName.
    def enterTypedefName(self, ctx:SimpleCParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by SimpleCParser#typedefName.
    def exitTypedefName(self, ctx:SimpleCParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by SimpleCParser#initializer.
    def enterInitializer(self, ctx:SimpleCParser.InitializerContext):
        pass

    # Exit a parse tree produced by SimpleCParser#initializer.
    def exitInitializer(self, ctx:SimpleCParser.InitializerContext):
        pass


    # Enter a parse tree produced by SimpleCParser#initializerList.
    def enterInitializerList(self, ctx:SimpleCParser.InitializerListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#initializerList.
    def exitInitializerList(self, ctx:SimpleCParser.InitializerListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#designation.
    def enterDesignation(self, ctx:SimpleCParser.DesignationContext):
        pass

    # Exit a parse tree produced by SimpleCParser#designation.
    def exitDesignation(self, ctx:SimpleCParser.DesignationContext):
        pass


    # Enter a parse tree produced by SimpleCParser#designatorList.
    def enterDesignatorList(self, ctx:SimpleCParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#designatorList.
    def exitDesignatorList(self, ctx:SimpleCParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#designator.
    def enterDesignator(self, ctx:SimpleCParser.DesignatorContext):
        pass

    # Exit a parse tree produced by SimpleCParser#designator.
    def exitDesignator(self, ctx:SimpleCParser.DesignatorContext):
        pass


    # Enter a parse tree produced by SimpleCParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:SimpleCParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleCParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:SimpleCParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleCParser#statement.
    def enterStatement(self, ctx:SimpleCParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#statement.
    def exitStatement(self, ctx:SimpleCParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#labeledStatement.
    def enterLabeledStatement(self, ctx:SimpleCParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#labeledStatement.
    def exitLabeledStatement(self, ctx:SimpleCParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#compoundStatement.
    def enterCompoundStatement(self, ctx:SimpleCParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#compoundStatement.
    def exitCompoundStatement(self, ctx:SimpleCParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#blockItemList.
    def enterBlockItemList(self, ctx:SimpleCParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#blockItemList.
    def exitBlockItemList(self, ctx:SimpleCParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by SimpleCParser#blockItem.
    def enterBlockItem(self, ctx:SimpleCParser.BlockItemContext):
        pass

    # Exit a parse tree produced by SimpleCParser#blockItem.
    def exitBlockItem(self, ctx:SimpleCParser.BlockItemContext):
        pass


    # Enter a parse tree produced by SimpleCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SimpleCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SimpleCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#selectionStatement.
    def enterSelectionStatement(self, ctx:SimpleCParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#selectionStatement.
    def exitSelectionStatement(self, ctx:SimpleCParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#iterationStatement.
    def enterIterationStatement(self, ctx:SimpleCParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#iterationStatement.
    def exitIterationStatement(self, ctx:SimpleCParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#jumpStatement.
    def enterJumpStatement(self, ctx:SimpleCParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by SimpleCParser#jumpStatement.
    def exitJumpStatement(self, ctx:SimpleCParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by SimpleCParser#compilationUnit.
    def enterCompilationUnit(self, ctx:SimpleCParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by SimpleCParser#compilationUnit.
    def exitCompilationUnit(self, ctx:SimpleCParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by SimpleCParser#translationUnit.
    def enterTranslationUnit(self, ctx:SimpleCParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by SimpleCParser#translationUnit.
    def exitTranslationUnit(self, ctx:SimpleCParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by SimpleCParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:SimpleCParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by SimpleCParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:SimpleCParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by SimpleCParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SimpleCParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SimpleCParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SimpleCParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SimpleCParser#declarationList.
    def enterDeclarationList(self, ctx:SimpleCParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by SimpleCParser#declarationList.
    def exitDeclarationList(self, ctx:SimpleCParser.DeclarationListContext):
        pass


