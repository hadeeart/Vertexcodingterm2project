import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

masterMaterial = AssetTools.create_asset("M_Master", "/Game/masterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color
baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial,unreal.MaterialExpressionTextureSampleParameter,-384,-300)
MaterialEditLibrary.connect_material_property(baseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create 2D Texture Param and Connect to Roughness
roughnessTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384.200)
MaterialEditLibrary.connect_material_property(roughnessTextureParam,"RGB", unreal.MaterialProperty.MP_ROUGHNESS)

#Create Constant Value and Connect to Specular
specParam = MaterialEditLibrary.create_material_expression(masterMaterial,unreal.MaterialExpressionConstant, -250.70)
specParam.set_editor_property("R",0.3)
MaterialEditLibrary.connect_material_property(specParam,"", unreal.MaterialProperty.MP_SPECULAR)

#create 2D Texture Param and Connect to Normal
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384. -100)
MaterialEditLibrary.connect_material_property(normalTextureParam,"RGB", unreal.MaterialProperty.MP_NORMAL)

#create 2D Texture Param and Connect to Metallic
metalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384. -0)
MaterialEditLibrary.connect_material_property(metalTextureParam,"RGB", unreal.MaterialProperty.MP_METALLIC)

#create 2D Texture Param and Connect to Ambient Ocullusion
aoTextureparam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, 100)
MaterialEditLibrary.connect_material_property(aoTextureparam,"RGB", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

EditorAssetLibrary.save_asset("/Game/masterMaterials/M_Master", True)