Sub CreateHypermeshNXArchitecture()
    Dim ppt As Object
    Dim slide As Object
    Dim shape As Object
    
    ' Get active presentation and slide
    Set ppt = Application.ActivePresentation
    Set slide = ppt.Slides.Add(ppt.Slides.Count + 1, ppLayoutBlank)
    
    ' Set slide background
    slide.Background.Fill.ForeColor.RGB = RGB(248, 250, 252)
    
    ' Title
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 200, 20, 600, 40)
    With shape.TextFrame.TextRange
        .Text = "AI Tool Architecture: Hypermesh-NX Sizing Loop"
        .Font.Name = "Arial"
        .Font.Size = 24
        .Font.Bold = True
        .Font.Color.RGB = RGB(30, 41, 59)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Flow Direction Indicator
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 50, 60, 750, 30)
    With shape
        .Fill.ForeColor.RGB = RGB(30, 41, 59)
        .Fill.Transparency = 0.9
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 65, 750, 20)
    With shape.TextFrame.TextRange
        .Text = "Main Data Flow Direction →"
        .Font.Name = "Arial"
        .Font.Size = 14
        .Font.Bold = True
        .Font.Color.RGB = RGB(30, 41, 59)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Step 1: Hypermesh
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 30, 120, 160, 120)
    With shape
        .Fill.ForeColor.RGB = RGB(59, 130, 246) ' Blue
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 30, 120, 160, 120)
    With shape.TextFrame.TextRange
        .Text = "Hypermesh" & vbCrLf & "FEA Model" & vbCrLf & vbCrLf & _
                "• Mesh Generation" & vbCrLf & _
                "• Material Properties" & vbCrLf & _
                "• Load Conditions"
        .Font.Name = "Arial"
        .Font.Size = 10
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 14
        .Lines(1).Font.Bold = True
        .Lines(2).Font.Size = 11
    End With
    
    ' Step Number 1
    Set shape = slide.Shapes.AddShape(msoShapeOval, 95, 100, 30, 30)
    With shape
        .Fill.ForeColor.RGB = RGB(30, 41, 59)
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 95, 100, 30, 30)
    With shape.TextFrame.TextRange
        .Text = "1"
        .Font.Name = "Arial"
        .Font.Size = 12
        .Font.Bold = True
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Step 2: TCL Extraction
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 230, 120, 160, 120)
    With shape
        .Fill.ForeColor.RGB = RGB(245, 158, 11) ' Orange
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 230, 120, 160, 120)
    With shape.TextFrame.TextRange
        .Text = "TCL Extraction" & vbCrLf & "Parameter Extraction" & vbCrLf & vbCrLf & _
                "• Geometry Parameters" & vbCrLf & _
                "• Material Thickness" & vbCrLf & _
                "• Element Properties" & vbCrLf & _
                "• Export to JSON"
        .Font.Name = "Arial"
        .Font.Size = 9
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 13
        .Lines(1).Font.Bold = True
        .Lines(2).Font.Size = 10
    End With
    
    ' Step Number 2
    Set shape = slide.Shapes.AddShape(msoShapeOval, 295, 100, 30, 30)
    With shape
        .Fill.ForeColor.RGB = RGB(30, 41, 59)
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 295, 100, 30, 30)
    With shape.TextFrame.TextRange
        .Text = "2"
        .Font.Name = "Arial"
        .Font.Size = 12
        .Font.Bold = True
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Step 3: Python Controller
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 430, 80, 180, 200)
    With shape
        .Fill.ForeColor.RGB = RGB(16, 185, 129) ' Green
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 430, 80, 180, 40)
    With shape.TextFrame.TextRange
        .Text = "Python Controller" & vbCrLf & "Core Orchestration"
        .Font.Name = "Arial"
        .Font.Size = 11
        .Font.Bold = True
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 14
    End With
    
    ' Python sub-components
    Dim subComponents As Variant
    subComponents = Array("JSON Parser", "Data Processor", "Loop Logic", "Sizing Engine", "API Manager", "Convergence", "NX Interface")
    Dim i As Integer
    Dim xPos As Integer
    Dim yPos As Integer
    
    For i = 0 To 6
        If i Mod 2 = 0 Then
            xPos = 440
        Else
            xPos = 520
        End If
        yPos = 145 + (Int(i / 2) * 35)
        
        Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, xPos, yPos, 80, 25)
        With shape
            .Fill.ForeColor.RGB = RGB(5, 150, 105)
            .Line.Visible = msoFalse
        End With
        Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, xPos, yPos, 80, 25)
        With shape.TextFrame.TextRange
            .Text = subComponents(i)
            .Font.Name = "Arial"
            .Font.Size = 8
            .Font.Color.RGB = RGB(255, 255, 255)
            .ParagraphFormat.Alignment = ppAlignCenter
        End With
    Next i
    
    ' Step Number 3
    Set shape = slide.Shapes.AddShape(msoShapeOval, 505, 60, 30, 30)
    With shape
        .Fill.ForeColor.RGB = RGB(30, 41, 59)
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 505, 60, 30, 30)
    With shape.TextFrame.TextRange
        .Text = "3"
        .Font.Name = "Arial"
        .Font.Size = 12
        .Font.Bold = True
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Step 4a: AI Vision Models
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 650, 50, 160, 100)
    With shape
        .Fill.ForeColor.RGB = RGB(139, 92, 246) ' Purple
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 650, 50, 160, 100)
    With shape.TextFrame.TextRange
        .Text = "AI Vision Models" & vbCrLf & vbCrLf & _
                "OpenAI GPT Vision" & vbCrLf & _
                "Pattern Analysis" & vbCrLf & _
                "Sizing Recommendations"
        .Font.Name = "Arial"
        .Font.Size = 10
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 12
        .Lines(1).Font.Bold = True
    End With
    
    ' Step 4b: Templates Engine
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 650, 180, 160, 100)
    With shape
        .Fill.ForeColor.RGB = RGB(99, 102, 241) ' Indigo
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 650, 180, 160, 100)
    With shape.TextFrame.TextRange
        .Text = "Templates Engine" & vbCrLf & vbCrLf & _
                "Design Templates" & vbCrLf & _
                "Sizing Rules" & vbCrLf & _
                "Optimization Logic"
        .Font.Name = "Arial"
        .Font.Size = 10
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 12
        .Lines(1).Font.Bold = True
    End With
    
    ' Step Number 4
    Set shape = slide.Shapes.AddShape(msoShapeOval, 715, 30, 30, 30)
    With shape
        .Fill.ForeColor.RGB = RGB(30, 41, 59)
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 715, 30, 30, 30)
    With shape.TextFrame.TextRange
        .Text = "4"
        .Font.Name = "Arial"
        .Font.Size = 12
        .Font.Bold = True
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Step 5: Siemens NX
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 850, 120, 180, 120)
    With shape
        .Fill.ForeColor.RGB = RGB(220, 38, 38) ' Red
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 850, 120, 180, 120)
    With shape.TextFrame.TextRange
        .Text = "Siemens NX" & vbCrLf & "CAD/CAE Platform" & vbCrLf & vbCrLf & _
                "• Geometry Updates" & vbCrLf & _
                "• Analysis Execution" & vbCrLf & _
                "• Results Generation"
        .Font.Name = "Arial"
        .Font.Size = 10
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 14
        .Lines(1).Font.Bold = True
        .Lines(2).Font.Size = 11
    End With
    
    ' Step Number 5
    Set shape = slide.Shapes.AddShape(msoShapeOval, 925, 100, 30, 30)
    With shape
        .Fill.ForeColor.RGB = RGB(30, 41, 59)
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 925, 100, 30, 30)
    With shape.TextFrame.TextRange
        .Text = "5"
        .Font.Name = "Arial"
        .Font.Size = 12
        .Font.Bold = True
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Supporting Components
    ' JSON Data Storage
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 430, 320, 180, 80)
    With shape
        .Fill.ForeColor.RGB = RGB(100, 116, 139) ' Gray
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 430, 320, 180, 80)
    With shape.TextFrame.TextRange
        .Text = "JSON Data Exchange" & vbCrLf & vbCrLf & _
                "• Parameter Storage" & vbCrLf & _
                "• Analysis Results" & vbCrLf & _
                "• Iteration History"
        .Font.Name = "Arial"
        .Font.Size = 10
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 12
        .Lines(1).Font.Bold = True
    End With
    
    ' C# Integration
    Set shape = slide.Shapes.AddShape(msoShapeRoundedRectangle, 650, 320, 160, 80)
    With shape
        .Fill.ForeColor.RGB = RGB(236, 72, 153) ' Pink
        .Line.Visible = msoFalse
    End With
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 650, 320, 160, 80)
    With shape.TextFrame.TextRange
        .Text = "C# Integration" & vbCrLf & vbCrLf & _
                ".NET Framework" & vbCrLf & _
                "NX Open API"
        .Font.Name = "Arial"
        .Font.Size = 11
        .Font.Color.RGB = RGB(255, 255, 255)
        .ParagraphFormat.Alignment = ppAlignCenter
        .Lines(1).Font.Size = 12
        .Lines(1).Font.Bold = True
    End With
    
    ' Main Flow Arrows
    CreateArrow slide, 190, 180, 230, 180, "Model", True
    CreateArrow slide, 390, 180, 430, 180, "JSON", True
    CreateArrow slide, 610, 150, 650, 110, "Analysis", True
    CreateArrow slide, 610, 220, 650, 230, "Rules", True
    CreateArrow slide, 810, 200, 850, 180, "Updates", True
    
    ' Supporting Arrows
    CreateArrow slide, 520, 280, 520, 320, "Store/Load", False
    CreateArrow slide, 770, 320, 900, 240, "API Calls", False
    
    ' Feedback Loop (Curved)
    Set shape = slide.Shapes.AddConnector(msoConnectorCurve, 940, 240, 500, 300)
    With shape.Line
        .ForeColor.RGB = RGB(239, 68, 68)
        .Weight = 3
        .DashStyle = msoLineDash
        .EndArrowheadStyle = msoArrowheadTriangle
    End With
    
    ' Feedback Loop Label
    Set shape = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 600, 420, 300, 20)
    With shape.TextFrame.TextRange
        .Text = "SIZING LOOP - Analysis Results Feedback"
        .Font.Name = "Arial"
        .Font.Size = 11
        .Font.Bold = True
        .Font.Color.RGB = RGB(239, 68, 68)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Create legends and workflow info
    CreateLegend slide
    CreateWorkflow slide
    
    MsgBox "Hypermesh-NX Architecture diagram created successfully!"
End Sub

Sub CreateArrow(slide As Object, x1 As Integer, y1 As Integer, x2 As Integer, y2 As Integer, labelText As String, isMain As Boolean)
    Dim arrow As Object
    Dim label As Object
    
    Set arrow = slide.Shapes.AddConnector(msoConnectorStraight, x1, y1, x2, y2)
    With arrow.Line
        If isMain Then
            .ForeColor.RGB = RGB(51, 51, 51)
            .Weight = 3
        Else
            .ForeColor.RGB = RGB(102, 102, 102)
            .Weight = 2
        End If
        .EndArrowheadStyle = msoArrowheadTriangle
    End With
    
    ' Add label
    Dim midX As Integer, midY As Integer
    midX = (x1 + x2) / 2
    midY = (y1 + y2) / 2 - 10
    
    Set label = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, midX - 25, midY, 50, 15)
    With label.TextFrame.TextRange
        .Text = labelText
        .Font.Name = "Arial"
        If isMain Then
            .Font.Size = 10
            .Font.Bold = True
        Else
            .Font.Size = 9
        End If
        .Font.Color.RGB = RGB(51, 51, 51)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
End Sub

Sub CreateLegend(slide As Object)
    Dim legend As Object
    Dim legendText As Object
    
    ' Legend background
    Set legend = slide.Shapes.AddShape(msoShapeRoundedRectangle, 600, 450, 320, 200)
    With legend
        .Fill.ForeColor.RGB = RGB(255, 255, 255)
        .Line.ForeColor.RGB = RGB(203, 213, 225)
        .Line.Weight = 1
    End With
    
    ' Legend title
    Set legendText = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 600, 460, 320, 20)
    With legendText.TextFrame.TextRange
        .Text = "Technology Stack"
        .Font.Name = "Arial"
        .Font.Size = 14
        .Font.Bold = True
        .Font.Color.RGB = RGB(30, 41, 59)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Legend items
    Dim legendItems As Variant
    Dim legendColors As Variant
    legendItems = Array("Hypermesh - FEA Pre-processing", "TCL - Parameter Extraction Scripts", _
                       "Python - Core Logic & Orchestration", "OpenAI Vision - AI Analysis", _
                       "Templates - Design Rules Engine", "Siemens NX - CAD/CAE Platform", _
                       "JSON - Data Exchange Format", "C# - NX API Integration")
    legendColors = Array(RGB(59, 130, 246), RGB(245, 158, 11), RGB(16, 185, 129), RGB(139, 92, 246), _
                        RGB(99, 102, 241), RGB(220, 38, 38), RGB(100, 116, 139), RGB(236, 72, 153))
    
    Dim i As Integer
    For i = 0 To 7
        ' Color dot
        Set legend = slide.Shapes.AddShape(msoShapeOval, 620, 490 + i * 20, 10, 10)
        With legend
            .Fill.ForeColor.RGB = legendColors(i)
            .Line.Visible = msoFalse
        End With
        
        ' Text
        Set legendText = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 635, 487 + i * 20, 280, 15)
        With legendText.TextFrame.TextRange
            .Text = legendItems(i)
            .Font.Name = "Arial"
            .Font.Size = 10
            .Font.Color.RGB = RGB(30, 41, 59)
        End With
    Next i
End Sub

Sub CreateWorkflow(slide As Object)
    Dim workflow As Object
    Dim workflowText As Object
    
    ' Workflow background
    Set workflow = slide.Shapes.AddShape(msoShapeRoundedRectangle, 50, 450, 500, 200)
    With workflow
        .Fill.ForeColor.RGB = RGB(255, 255, 255)
        .Line.ForeColor.RGB = RGB(203, 213, 225)
        .Line.Weight = 1
    End With
    
    ' Workflow title
    Set workflowText = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 50, 460, 500, 20)
    With workflowText.TextFrame.TextRange
        .Text = "Sequential Workflow Process"
        .Font.Name = "Arial"
        .Font.Size = 14
        .Font.Bold = True
        .Font.Color.RGB = RGB(30, 41, 59)
        .ParagraphFormat.Alignment = ppAlignCenter
    End With
    
    ' Workflow steps
    Set workflowText = slide.Shapes.AddTextbox(msoTextOrientationHorizontal, 60, 485, 480, 155)
    With workflowText.TextFrame.TextRange
        .Text = "Step 1 - Hypermesh:" & vbCrLf & _
                "• Generate finite element model" & vbCrLf & _
                "• Define materials, loads, and boundary conditions" & vbCrLf & vbCrLf & _
                "Step 2 - TCL Parameter Extraction:" & vbCrLf & _
                "• Execute TCL scripts to extract model parameters" & vbCrLf & _
                "• Parse geometry, material, and element properties" & vbCrLf & vbCrLf & _
                "Step 3 - Python Data Controller:" & vbCrLf & _
                "• Process JSON data and initialize sizing loop" & vbCrLf & _
                "• Coordinate between AI models and templates" & vbCrLf & vbCrLf & _
                "Step 4 - Templates & AI Processing:" & vbCrLf & _
                "• AI vision analyzes stress patterns and failure modes" & vbCrLf & _
                "• Templates apply design rules and optimization logic" & vbCrLf & vbCrLf & _
                "Step 5 - NX Implementation:" & vbCrLf & _
                "• Update geometry with new sizing parameters" & vbCrLf & _
                "• Execute analysis and generate results for next iteration"
        .Font.Name = "Arial"
        .Font.Size = 9
        .Font.Color.RGB = RGB(71, 85, 105)
        
        ' Make step headers bold and colored
        .Lines(1).Font.Bold = True
        .Lines(1).Font.Color.RGB = RGB(59, 130, 246)
        .Lines(5).Font.Bold = True
        .Lines(5).Font.Color.RGB = RGB(245, 158, 11)
        .Lines(9).Font.Bold = True
        .Lines(9).Font.Color.RGB = RGB(16, 185, 129)
        .Lines(13).Font.Bold = True
        .Lines(13).Font.Color.RGB = RGB(139, 92, 246)
        .Lines(17).Font.Bold = True
        .Lines(17).Font.Color.RGB = RGB(220, 38, 38)
    End With
End Sub