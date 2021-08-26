#region Miscellaneous commands
import context_menu
context_menu.DoSuppressModelEnvItem(ExtAPI)
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInsertMeshElementShape(ExtAPI)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [69]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_AutomaticMethod_1 = ExtAPI.DataModel.GetObjectById(49)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [69]
_AutomaticMethod_1.Location = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property

_AutomaticMethod_1.Method = MethodType.Sweep
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInsertMeshElementShape(ExtAPI)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [70]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_AutomaticMethod_2 = ExtAPI.DataModel.GetObjectById(51)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [70]
_AutomaticMethod_2.Location = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property

_AutomaticMethod_2.Method = MethodType.AllTriAllTet
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInsertMeshElementShape(ExtAPI)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [186]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_AutomaticMethod_3 = ExtAPI.DataModel.GetObjectById(53)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [186]
_AutomaticMethod_3.Location = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property

_AutomaticMethod_3.Method = MethodType.AllTriAllTet
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [186]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInflateSelection(ExtAPI)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [185]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_Inflation_1 = ExtAPI.DataModel.GetObjectById(55)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [185]
_Inflation_1.BoundaryLocation = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInsertMeshElementShape(ExtAPI)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [5]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_AutomaticMethod_4 = ExtAPI.DataModel.GetObjectById(58)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [5]
_AutomaticMethod_4.Location = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property

_AutomaticMethod_4.Method = MethodType.AllTriAllTet
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [5]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInflateSelection(ExtAPI)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [4]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_Inflation_2 = ExtAPI.DataModel.GetObjectById(60)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [4]
_Inflation_2.BoundaryLocation = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInsertMeshElementShape(ExtAPI)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [202]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_AutomaticMethod_5 = ExtAPI.DataModel.GetObjectById(63)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [202]
_AutomaticMethod_5.Location = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property

_AutomaticMethod_5.Method = MethodType.AllTriAllTet
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [202]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Miscellaneous commands
import context_menu
context_menu.DoInflateSelection(ExtAPI)
#endregion

#region Set object property
_Inflation_3 = ExtAPI.DataModel.GetObjectById(65)
_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = []
_Inflation_3.BoundaryLocation = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = [201]
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property

_wb_jnl_seln = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
_wb_jnl_seln.Ids = [201]
_Inflation_3.BoundaryLocation = _wb_jnl_seln
#endregion

#region Set current scoping selection
currentSelection = ExtAPI.SelectionManager.CreateSelectionInfo(Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities)
currentSelection.Ids = []
ExtAPI.SelectionManager.NewSelection(currentSelection)
#endregion

#region Set object property
_Mesh_1 = ExtAPI.DataModel.GetObjectById(12)
_Mesh_1.ElementSize =  Quantity(0.1, "m")
#endregion


