@ stdcall AbortDoc(ptr)
@ stdcall AbortPath(ptr)
@ stdcall AddFontMemResourceEx(ptr long ptr ptr)
@ stdcall AddFontResourceA(str)
@ stdcall AddFontResourceExA(str long ptr)
@ stdcall AddFontResourceExW(wstr long ptr)
@ stdcall AddFontResourceTracking(str long)
@ stdcall AddFontResourceW(wstr)
@ stdcall AngleArc(ptr long long long long long)
@ stdcall AnimatePalette(long long long ptr)
@ stdcall AnyLinkedFonts() 
@ stdcall Arc(long long long long long long long long long)
@ stdcall ArcTo(long long long long long long long long long)
@ stdcall BRUSHOBJ_hGetColorTransform(ptr)
@ stdcall BRUSHOBJ_pvAllocRbrush(ptr long)
@ stdcall BRUSHOBJ_pvGetRbrush(ptr) 
@ stdcall BRUSHOBJ_ulGetBrushColor(ptr) 
@ stdcall BeginPath(long)
@ stdcall BitBlt(long long long long long long long long long)
@ stdcall CLIPOBJ_bEnum(ptr long long) 
@ stdcall CLIPOBJ_cEnumStart(ptr long long long long) 
@ stdcall CLIPOBJ_ppoGetPath(ptr) 
@ stdcall CancelDC(long)
@ stdcall CheckColorsInGamut(ptr ptr ptr long)
@ stdcall ChoosePixelFormat(long ptr)
@ stdcall Chord(long long long long long long long long long)
@ stdcall ClearBitmapAttributes(ptr long)
@ stdcall ClearBrushAttributes(ptr long)
@ stdcall CloseEnhMetaFile(long)
@ stdcall CloseFigure(long)
@ stdcall CloseMetaFile(long)
@ stdcall ColorCorrectPalette(ptr ptr long long)
@ stdcall ColorMatchToTarget(ptr ptr long)
@ stdcall CombineRgn(long long long long)
@ stdcall CombineTransform(ptr ptr ptr)
@ stdcall CopyEnhMetaFileA(long str)
@ stdcall CopyEnhMetaFileW(long wstr)
@ stdcall CopyMetaFileA(long str)
@ stdcall CopyMetaFileW(long wstr)
@ stdcall CreateBitmap(long long long long ptr)
@ stdcall CreateBitmapIndirect(ptr)
@ stdcall CreateBrushIndirect(ptr)
@ stdcall CreateColorSpaceA(ptr)
@ stdcall CreateColorSpaceW(ptr)
@ stdcall CreateCompatibleBitmap(long long long)
@ stdcall CreateCompatibleDC(long)
@ stdcall CreateDCA(str str str ptr)
@ stdcall CreateDCW(wstr wstr wstr ptr)
@ stdcall CreateDIBPatternBrush(long long)
@ stdcall CreateDIBPatternBrushPt(long long)
@ stdcall CreateDIBSection(long ptr long ptr long long)
@ stdcall CreateDIBitmap(long ptr long ptr ptr long)
@ stdcall CreateDiscardableBitmap(long long long)
@ stdcall CreateEllipticRgn(long long long long)
@ stdcall CreateEllipticRgnIndirect(ptr)
@ stdcall CreateEnhMetaFileA(long str ptr str)
@ stdcall CreateEnhMetaFileW(long wstr ptr wstr)
@ stdcall CreateFontA(long long long long long long long long long long long long long str)
@ stdcall CreateFontIndirectA(ptr)
@ stdcall CreateFontIndirectExA(ptr)
@ stdcall CreateFontIndirectExW(ptr)
@ stdcall CreateFontIndirectW(ptr)
@ stdcall CreateFontW(long long long long long long long long long long long long long wstr)
@ stdcall CreateHalftonePalette(long) 
@ stdcall CreateHatchBrush(long long)
@ stdcall CreateICA(str str str ptr)
@ stdcall CreateICW(wstr wstr wstr ptr)
@ stdcall CreateMetaFileA(str)
@ stdcall CreateMetaFileW(wstr)
@ stdcall CreatePalette(ptr)
@ stdcall CreatePatternBrush(long)
@ stdcall CreatePen(long long long)
@ stdcall CreatePenIndirect(ptr)
@ stdcall CreatePolyPolygonRgn(ptr ptr long long)
@ stdcall CreatePolygonRgn(ptr long long)
@ stdcall CreateRectRgn(long long long long)
@ stdcall CreateRectRgnIndirect(ptr)
@ stdcall CreateRoundRectRgn(long long long long long long) 
@ stdcall CreateScalableFontResourceA(long str str str)
@ stdcall CreateScalableFontResourceW(long wstr wstr wstr)
@ stdcall CreateSolidBrush(long)
@ stdcall DPtoLP(long ptr long)
@ stdcall DdEntry0(ptr ptr ptr ptr ptr ptr) 
@ stdcall DdEntry10(ptr ptr) 
@ stdcall DdEntry11(ptr ptr ptr) 
@ stdcall DdEntry12(ptr ptr) 
@ stdcall DdEntry13(ptr ptr) 
@ stdcall DdEntry14(ptr ptr) 
@ stdcall DdEntry15(ptr)
@ stdcall DdEntry16(ptr ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall DdEntry17(ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall DdEntry18(ptr ptr) 
@ stdcall DdEntry19(ptr ptr ptr ptr ptr long) 
@ stdcall DdEntry1(ptr ptr ptr ptr) 
@ stdcall DdEntry20(ptr) 
@ stdcall DdEntry21(ptr) 
@ stdcall DdEntry22(ptr ptr) 
@ stdcall DdEntry23(ptr long) 
@ stdcall DdEntry24(ptr)
@ stdcall DdEntry25(ptr ptr) 
@ stdcall DdEntry26(ptr ptr ptr ptr ptr)
@ stdcall DdEntry27(ptr long) 
@ stdcall DdEntry28(ptr ptr) 
@ stdcall DdEntry29(ptr ptr) 
@ stdcall DdEntry2(ptr) 
@ stdcall DdEntry30(ptr ptr)
@ stdcall DdEntry31(ptr ptr) 
@ stdcall DdEntry32(ptr ptr long) 
@ stdcall DdEntry33(ptr ptr)
@ stdcall DdEntry34(ptr ptr) 
@ stdcall DdEntry35(ptr ptr) 
@ stdcall DdEntry36(ptr ptr)
@ stdcall DdEntry37(ptr ptr)
@ stdcall DdEntry38(ptr ptr) 
@ stdcall DdEntry39(ptr ptr ptr) 
@ stdcall DdEntry3(ptr) 
@ stdcall DdEntry40(ptr ptr) 
@ stdcall DdEntry41(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall DdEntry42(ptr ptr) 
@ stdcall DdEntry43(ptr ptr) 
@ stdcall DdEntry44(ptr) 
@ stdcall DdEntry45(ptr ptr) 
@ stdcall DdEntry46(ptr ptr) 
@ stdcall DdEntry47(ptr ptr) 
@ stdcall DdEntry48(ptr ptr) 
@ stdcall DdEntry49(ptr ptr ptr) 
@ stdcall DdEntry4(ptr) 
@ stdcall DdEntry50(ptr ptr long) 
@ stdcall DdEntry51(ptr ptr ptr) 
@ stdcall DdEntry52(ptr ptr) 
@ stdcall DdEntry53(ptr ptr) 
@ stdcall DdEntry54(ptr ptr) 
@ stdcall DdEntry55(ptr ptr long) 
@ stdcall DdEntry56(ptr ptr) 
@ stdcall DdEntry5(ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall DdEntry6(ptr) 
@ stdcall DdEntry7(ptr ptr ptr) 
@ stdcall DdEntry8(ptr ptr ptr) 
@ stdcall DdEntry9(ptr ptr) 
@ stdcall DeleteColorSpace(long) 
@ stdcall DeleteDC(long)
@ stdcall DeleteEnhMetaFile(long)
@ stdcall DeleteMetaFile(long)
@ stdcall DeleteObject(long)
@ stdcall DescribePixelFormat(long long long ptr)
@ stdcall DeviceCapabilitiesExA(str str long str ptr)
@ stdcall DeviceCapabilitiesExW(wstr wstr long wstr ptr)
@ stdcall DrawEscape(long long long ptr)
@ stdcall Ellipse(long long long long long)
@ stdcall EnableEUDC(long) 
@ stdcall EndDoc(long)
@ stdcall EndFormPage(ptr)
@ stdcall EndPage(long)
@ stdcall EndPath(long)
@ stdcall EngAcquireSemaphore(ptr)
@ stdcall EngAlphaBlend(ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall EngAssociateSurface(ptr ptr long) 
@ stdcall EngBitBlt(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall EngCheckAbort(ptr) 
@ stdcall EngComputeGlyphSet(ptr ptr ptr)
@ stdcall EngCopyBits(ptr ptr ptr ptr ptr ptr) 
@ stdcall EngCreateBitmap(int64 long long long ptr) 
@ stdcall EngCreateClip() 
@ stdcall EngCreateDeviceBitmap(ptr int64 long) 
@ stdcall EngCreateDeviceSurface(ptr int64 long) 
@ stdcall EngCreatePalette(long long ptr long long long) 
@ stdcall EngCreateSemaphore()
@ stdcall EngDeleteClip(ptr) 
@ stdcall EngDeletePalette(ptr) 
@ stdcall EngDeletePath(ptr) 
@ stdcall EngDeleteSemaphore(ptr)
@ stdcall EngDeleteSurface(ptr) 
@ stdcall EngEraseSurface(ptr ptr long) 
@ stdcall EngFillPath(ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall EngFindResource(ptr long long ptr)
@ stdcall EngFreeModule(ptr)
@ stdcall EngGetCurrentCodePage(ptr ptr)
@ stdcall EngGetDriverName(ptr)
@ stdcall EngGetPrinterDataFileName(ptr)
@ stdcall EngGradientFill(ptr ptr ptr ptr long ptr long ptr ptr long) 
@ stdcall EngLineTo(ptr ptr ptr long long long long ptr ptr) 
@ stdcall EngLoadModule(ptr)
@ stdcall EngLockSurface(ptr) 
@ stdcall EngMarkBandingSurface(ptr) 
@ stdcall EngMultiByteToUnicodeN(wstr long ptr str long) RtlMultiByteToUnicodeN
@ stdcall EngMultiByteToWideChar(long wstr long str long)
@ stdcall EngPaint(ptr ptr ptr ptr ptr) 
@ stdcall EngPlgBlt(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr long) 
@ stdcall EngQueryEMFInfo(ptr ptr)
@ stdcall EngQueryLocalTime(ptr)
@ stdcall EngReleaseSemaphore(ptr)
@ stdcall EngStretchBlt(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr long) 
@ stdcall EngStretchBltROP(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr long ptr long) 
@ stdcall EngStrokeAndFillPath(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall EngStrokePath(ptr ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall EngTextOut(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr) 
@ stdcall EngTransparentBlt(ptr ptr ptr ptr ptr ptr long long) 
@ stdcall EngUnicodeToMultiByteN(str long long wstr long) RtlUnicodeToMultiByteN
@ stdcall EngUnlockSurface(ptr) 
@ stdcall EngWideCharToMultiByte(long wstr long str long)
@ stdcall EnumEnhMetaFile(long long ptr ptr ptr)
@ stdcall EnumFontFamiliesA(long str ptr long)
@ stdcall EnumFontFamiliesExA(long ptr ptr long long)
@ stdcall EnumFontFamiliesExW(long ptr ptr long long)
@ stdcall EnumFontFamiliesW(long wstr ptr long)
@ stdcall EnumFontsA(long str ptr long)
@ stdcall EnumFontsW(long wstr ptr long)
@ stdcall EnumICMProfilesA(long ptr long)
@ stdcall EnumICMProfilesW(long ptr long)
@ stdcall EnumMetaFile(long long ptr ptr)
@ stdcall EnumObjects(long long ptr long)
@ stdcall EqualRgn(long long) 
@ stdcall Escape(long long long ptr ptr)
@ stdcall EudcLoadLinkW(wstr wstr long long)
@ stdcall EudcUnloadLinkW(wstr wstr)
@ stdcall ExcludeClipRect(long long long long long)
@ stdcall ExtCreatePen(long long ptr long ptr)
@ stdcall ExtCreateRegion(ptr long ptr)
@ stdcall ExtEscape(long long long ptr long ptr)
@ stdcall ExtFloodFill(long long long long long)
@ stdcall ExtSelectClipRgn(long long long)
@ stdcall ExtTextOutA(long long long long ptr str long ptr)
@ stdcall ExtTextOutW(long long long long ptr wstr long ptr)
@ stdcall FONTOBJ_cGetAllGlyphHandles(ptr ptr) 
@ stdcall FONTOBJ_cGetGlyphs(ptr long long ptr ptr) 
@ stdcall FONTOBJ_pQueryGlyphAttrs(ptr long) 
@ stdcall FONTOBJ_pfdg(ptr) 
@ stdcall FONTOBJ_pifi(ptr) 
@ stdcall FONTOBJ_pvTrueTypeFontFile(ptr ptr) 
@ stdcall FONTOBJ_pxoGetXform(ptr) 
@ stdcall FONTOBJ_vGetInfo(ptr long ptr) 
@ stdcall FillPath(long)
@ stdcall FillRgn(long long long)
@ stdcall FixBrushOrgEx(long long long ptr)
@ stdcall FlattenPath(long)
@ stdcall FloodFill(long long long long)
@ stdcall FontIsLinked(long) 
@ stdcall FrameRgn(long long long long long)
@ stdcall GdiAddFontResourceW(ptr ptr ptr)
@ stdcall GdiAddGlsBounds(ptr ptr)
@ stdcall GdiAddGlsRecord(ptr long ptr ptr)
@ stdcall GdiAlphaBlend(long long long long long long long long long long long)
@ stdcall GdiArtificialDecrementDriver(wstr long)
@ stdcall GdiCleanCacheDC(ptr)
@ stdcall GdiComment(long long ptr)
@ stdcall GdiConsoleTextOut(ptr ptr long ptr) 
@ stdcall GdiConvertAndCheckDC(ptr)
@ stdcall GdiConvertBitmap(ptr)
@ stdcall GdiConvertBitmapV5(ptr ptr long long)
@ stdcall GdiConvertBrush(ptr)
@ stdcall GdiConvertDC(ptr)
@ stdcall GdiConvertEnhMetaFile(ptr)
@ stdcall GdiConvertFont(ptr)
@ stdcall GdiConvertMetaFilePict(ptr)
@ stdcall GdiConvertPalette(ptr)
@ stdcall GdiConvertRegion(ptr)
@ stdcall GdiConvertToDevmodeW(ptr)
@ stdcall GdiCreateLocalEnhMetaFile(ptr)
@ stdcall GdiCreateLocalMetaFilePict(ptr)
@ stdcall GdiDeleteLocalDC(ptr)
@ stdcall GdiDeleteSpoolFileHandle(ptr)
@ stdcall GdiDescribePixelFormat(ptr long long ptr) 
@ stdcall GdiDllInitialize(ptr long ptr)
@ stdcall GdiDrawStream(ptr long ptr)
@ stdcall GdiEndDocEMF(ptr)
@ stdcall GdiEndPageEMF(ptr long)
@ stdcall GdiEntry10(ptr long)
@ stdcall GdiEntry11(ptr ptr)
@ stdcall GdiEntry12(ptr ptr)
@ stdcall GdiEntry13()
@ stdcall GdiEntry14(ptr ptr long)
@ stdcall GdiEntry15(ptr ptr ptr)
@ stdcall GdiEntry16(ptr ptr ptr)
@ stdcall GdiEntry1(ptr ptr)
@ stdcall GdiEntry2(ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr ptr)
@ stdcall GdiEntry3(ptr)
@ stdcall GdiEntry4(ptr long)
@ stdcall GdiEntry5(ptr)
@ stdcall GdiEntry6(ptr ptr)
@ stdcall GdiEntry7(ptr ptr)
@ stdcall GdiEntry8(ptr)
@ stdcall GdiEntry9(ptr ptr ptr ptr ptr ptr)
@ stdcall GdiFixUpHandle(ptr)
@ stdcall GdiFlush()
@ stdcall GdiFullscreenControl(ptr ptr long ptr ptr) 
@ stdcall GdiGetBatchLimit()
@ stdcall GdiGetCharDimensions(long ptr ptr)
@ stdcall GdiGetCodePage(long)
@ stdcall GdiGetDC(ptr)
@ stdcall GdiGetDevmodeForPage(ptr long ptr ptr)
@ stdcall GdiGetLocalBrush(ptr)
@ stdcall GdiGetLocalDC(ptr)
@ stdcall GdiGetLocalFont(ptr)
@ stdcall GdiGetPageCount(ptr)
@ stdcall GdiGetPageHandle(ptr long ptr)
@ stdcall GdiGetSpoolFileHandle(wstr ptr wstr)
@ stdcall GdiGetSpoolMessage(ptr long ptr long) 
@ stdcall GdiGradientFill(long ptr long ptr long long)
@ stdcall GdiInitSpool() 
@ stdcall GdiInitializeLanguagePack(long)
@ stdcall GdiIsMetaFileDC(long)
@ stdcall GdiIsMetaPrintDC(long)
@ stdcall GdiIsPlayMetafileDC(long)
@ stdcall GdiPlayDCScript(long long long long long long)
@ stdcall GdiPlayEMF(wstr ptr wstr ptr ptr)
@ stdcall GdiPlayJournal(long long long long long)
@ stdcall GdiPlayPageEMF(ptr ptr ptr ptr ptr)
@ stdcall GdiPlayPrivatePageEMF(ptr long ptr)
@ stdcall GdiPlayScript(ptr ptr ptr ptr ptr ptr ptr)
@ stdcall GdiPrinterThunk(ptr ptr long)
@ stdcall GdiProcessSetup()
@ stdcall GdiQueryFonts(ptr long ptr) 
@ stdcall GdiQueryTable()
@ stdcall GdiRealizationInfo(long ptr)
@ stdcall GdiReleaseDC(ptr)
@ stdcall GdiReleaseLocalDC(ptr)
@ stdcall GdiResetDCEMF(ptr ptr)
@ stdcall GdiSetAttrs(ptr)
@ stdcall GdiSetBatchLimit(long)
@ stdcall GdiSetLastError(long)
@ stdcall GdiSetPixelFormat(ptr long) 
@ stdcall GdiSetServerAttr(ptr long)
@ stdcall GdiStartDocEMF(ptr ptr)
@ stdcall GdiStartPageEMF(ptr)
@ stdcall GdiSwapBuffers(ptr) 
@ stdcall GdiTransparentBlt(long long long long long long long long long long long)
@ stdcall GdiValidateHandle(ptr)
@ stdcall GetArcDirection(long)
@ stdcall GetAspectRatioFilterEx(long ptr)
@ stdcall GetBitmapAttributes(ptr)
@ stdcall GetBitmapBits(long long ptr) 
@ stdcall GetBitmapDimensionEx(long ptr) 
@ stdcall GetBkColor(long)
@ stdcall GetBkMode(long)
@ stdcall GetBoundsRect(long ptr long)
@ stdcall GetBrushAttributes(ptr)
@ stdcall GetBrushOrgEx(long ptr)
@ stdcall GetCharABCWidthsA(long long long ptr)
@ stdcall GetCharABCWidthsFloatA(long long long ptr)
@ stdcall GetCharABCWidthsFloatW(long long long ptr)
@ stdcall GetCharABCWidthsI(long long long ptr ptr)
@ stdcall GetCharABCWidthsW(long long long ptr)
@ stdcall GetCharWidth32A(long long long long)
@ stdcall GetCharWidth32W(long long long long)
@ stdcall GetCharWidthA(long long long long) GetCharWidth32A
@ stdcall GetCharWidthFloatA(long long long ptr)
@ stdcall GetCharWidthFloatW(long long long ptr)
@ stdcall GetCharWidthI(ptr long long ptr ptr)
@ stdcall GetCharWidthInfo(ptr ptr) 
@ stdcall GetCharWidthW(long long long long)
@ stdcall GetCharacterPlacementA(long str long long ptr long)
@ stdcall GetCharacterPlacementW(long wstr long long ptr long)
@ stdcall GetClipBox(long ptr)
@ stdcall GetClipRgn(long long)
@ stdcall GetColorAdjustment(long ptr) 
@ stdcall GetColorSpace(long)
@ stdcall GetCurrentObject(long long)
@ stdcall GetCurrentPositionEx(long ptr)
@ stdcall GetDCBrushColor(ptr)
@ stdcall GetDCOrgEx(ptr ptr)
@ stdcall GetDCPenColor(long)
@ stdcall GetDIBColorTable(long long long ptr)
@ stdcall GetDIBits(long long long long ptr ptr long)
@ stdcall GetDeviceCaps(long long)
@ stdcall GetDeviceGammaRamp(long ptr)
@ stdcall GetETM(ptr ptr)
@ stdcall GetEUDCTimeStamp()
@ stdcall GetEUDCTimeStampExW(str)
@ stdcall GetEnhMetaFileA(str)
@ stdcall GetEnhMetaFileBits(long long ptr)
@ stdcall GetEnhMetaFileDescriptionA(long long ptr)
@ stdcall GetEnhMetaFileDescriptionW(long long ptr)
@ stdcall GetEnhMetaFileHeader(long long ptr)
@ stdcall GetEnhMetaFilePaletteEntries (long long ptr)
@ stdcall GetEnhMetaFilePixelFormat(ptr long ptr)
@ stdcall GetEnhMetaFileW(wstr)
@ stdcall GetFontAssocStatus(ptr)
@ stdcall GetFontData(long long long ptr long)
@ stdcall GetFontLanguageInfo(long)
@ stdcall GetFontResourceInfoW(str ptr ptr long)
@ stdcall GetFontUnicodeRanges(ptr ptr) 
@ stdcall GetGlyphIndicesA(long ptr long ptr long)
@ stdcall GetGlyphIndicesW(long ptr long ptr long) 
@ stdcall GetGlyphOutline(long long long ptr long ptr ptr) GetGlyphOutlineA
@ stdcall GetGlyphOutlineA(long long long ptr long ptr ptr)
@ stdcall GetGlyphOutlineW(long long long ptr long ptr ptr)
@ stdcall GetGlyphOutlineWow(long long long long long long long)
@ stdcall GetGraphicsMode(long)
@ stdcall GetHFONT(ptr)
@ stdcall GetICMProfileA(long ptr ptr)
@ stdcall GetICMProfileW(long ptr ptr)
@ stdcall GetKerningPairs(long long ptr) GetKerningPairsA
@ stdcall GetKerningPairsA(long long ptr)
@ stdcall GetKerningPairsW(long long ptr)
@ stdcall GetLayout(long)
@ stdcall GetLogColorSpaceA(long ptr long)
@ stdcall GetLogColorSpaceW(long ptr long)
@ stdcall GetMapMode(long)
@ stdcall GetMetaFileA(str)
@ stdcall GetMetaFileBitsEx(long long ptr)
@ stdcall GetMetaFileW(wstr)
@ stdcall GetMetaRgn(long long)
@ stdcall GetMiterLimit(long ptr) 
@ stdcall GetNearestColor(long long) 
@ stdcall GetNearestPaletteIndex(long long) 
@ stdcall GetObjectA(long long ptr)
@ stdcall GetObjectType(long)
@ stdcall GetObjectW(long long ptr)
@ stdcall GetOutlineTextMetricsA(long long ptr)
@ stdcall GetOutlineTextMetricsW(long long ptr)
@ stdcall GetPaletteEntries(long long long ptr)
@ stdcall GetPath(long ptr ptr long)
@ stdcall GetPixel(long long long)
@ stdcall GetPixelFormat(long)
@ stdcall GetPolyFillMode(long)
@ stdcall GetROP2(long)
@ stdcall GetRandomRgn(long long long) 
@ stdcall GetRasterizerCaps(ptr long) 
@ stdcall GetRegionData(long long ptr)
@ stdcall GetRelAbs(long long)
@ stdcall GetRgnBox(long ptr)
@ stdcall GetStockObject(long)
@ stdcall GetStretchBltMode(long)
@ stdcall GetStringBitmapA(ptr str long long ptr)
@ stdcall GetStringBitmapW(ptr wstr long long ptr)
@ stdcall GetSystemPaletteEntries(long long long ptr)
@ stdcall GetSystemPaletteUse(long) 
@ stdcall GetTextAlign(long)
@ stdcall GetTextCharacterExtra(long)
@ stdcall GetTextCharset(long)
@ stdcall GetTextCharsetInfo(long ptr long) 
@ stdcall GetTextColor(long)
@ stdcall GetTextExtentExPointA(long str long long ptr ptr ptr)
@ stdcall GetTextExtentExPointI(long ptr long long ptr ptr ptr)
@ stdcall GetTextExtentExPointW(long wstr long long ptr ptr ptr)
@ stdcall GetTextExtentExPointWPri(ptr wstr long long long ptr ptr)
@ stdcall GetTextExtentPoint32A(long str long ptr)
@ stdcall GetTextExtentPoint32W(long wstr long ptr)
@ stdcall GetTextExtentPointA(long str long ptr)
@ stdcall GetTextExtentPointI(long ptr long ptr)
@ stdcall GetTextExtentPointW(long wstr long ptr)
@ stdcall GetTextFaceA(long long ptr)
@ stdcall GetTextFaceAliasW(ptr long wstr)
@ stdcall GetTextFaceW(long long ptr)
@ stdcall GetTextMetricsA(long ptr)
@ stdcall GetTextMetricsW(long ptr)
@ stdcall GetTransform(long long ptr) 
@ stdcall GetViewportExtEx(long ptr)
@ stdcall GetViewportOrgEx(long ptr)
@ stdcall GetWinMetaFileBits(long long ptr long long)
@ stdcall GetWindowExtEx(long ptr)
@ stdcall GetWindowOrgEx(long ptr)
@ stdcall GetWorldTransform(long ptr)
@ stdcall HT_Get8BPPFormatPalette(ptr long long long) 
@ stdcall HT_Get8BPPMaskPalette(ptr long long long long long) 
@ stdcall IntersectClipRect(long long long long long)
@ stdcall InvertRgn(long long)
@ stdcall IsValidEnhMetaRecord(long long) gdibase.IsValidEnhMetaRecord
@ stdcall IsValidEnhMetaRecordOffExt(long long long long) gdibase.IsValidEnhMetaRecordOffExt
@ stdcall LPtoDP(long ptr long)
@ stdcall LineDDA(long long long long ptr long)
@ stdcall LineTo(long long long)
@ stdcall MaskBlt(long long long long long long long long long long long long)
@ stdcall MirrorRgn(ptr ptr)
@ stdcall ModifyWorldTransform(long ptr long)
@ stdcall MoveToEx(long long long ptr)
@ stdcall NamedEscape(ptr wstr long long str long str)
@ stdcall OffsetClipRgn(long long long)
@ stdcall OffsetRgn(long long long)
@ stdcall OffsetViewportOrgEx(long long long ptr)
@ stdcall OffsetWindowOrgEx(long long long ptr)
@ stdcall PATHOBJ_bEnum(ptr ptr) 
@ stdcall PATHOBJ_bEnumClipLines(ptr long ptr) 
@ stdcall PATHOBJ_vEnumStart(ptr) 
@ stdcall PATHOBJ_vEnumStartClipLines(ptr ptr ptr ptr) 
@ stdcall PATHOBJ_vGetBounds(ptr ptr) 
@ stdcall PaintRgn(long long)
@ stdcall PatBlt(long long long long long long)
@ stdcall PathToRegion(long)
@ stdcall Pie(long long long long long long long long long)
@ stdcall PlayEnhMetaFile(long long ptr)
@ stdcall PlayEnhMetaFileRecord(long ptr ptr long)
@ stdcall PlayMetaFile(long long)
@ stdcall PlayMetaFileRecord(long ptr ptr long)
@ stdcall PlgBlt(long ptr long long long long long long long long)
@ stdcall PolyBezier(long ptr long)
@ stdcall PolyBezierTo(long ptr long)
@ stdcall PolyDraw(long ptr ptr long)
@ stdcall PolyPatBlt(ptr long ptr long long)
@ stdcall PolyPolygon(long ptr ptr long)
@ stdcall PolyPolyline(long ptr ptr long)
@ stdcall PolyTextOutA(long ptr long)
@ stdcall PolyTextOutW(long ptr long)
@ stdcall Polygon(long ptr long)
@ stdcall Polyline(long ptr long)
@ stdcall PolylineTo(long ptr long)
@ stdcall PtInRegion(long long long)
@ stdcall PtVisible(long long long) 
@ stdcall QueryFontAssocStatus()
@ stdcall RealizePalette(long)
@ stdcall RectInRegion(long ptr)
@ stdcall RectVisible(long ptr) 
@ stdcall Rectangle(long long long long long)
@ stdcall RemoveFontMemResourceEx(ptr)
@ stdcall RemoveFontResourceA(str)
@ stdcall RemoveFontResourceExA(str long ptr)
@ stdcall RemoveFontResourceExW(wstr long ptr)
@ stdcall RemoveFontResourceTracking(ptr long)
@ stdcall RemoveFontResourceW(wstr)
@ stdcall ResetDCA(long ptr)
@ stdcall ResetDCW(long ptr)
@ stdcall ResizePalette(long long)
@ stdcall RestoreDC(long long)
@ stdcall RoundRect(long long long long long long long)
@ stdcall STROBJ_bEnum(ptr ptr ptr) 
@ stdcall STROBJ_bEnumPositionsOnly(ptr ptr ptr) 
@ stdcall STROBJ_bGetAdvanceWidths(ptr long long ptr) 
@ stdcall STROBJ_dwGetCodePage(ptr) 
@ stdcall STROBJ_vEnumStart(ptr) 
@ stdcall SaveDC(long)
@ stdcall ScaleViewportExtEx(long long long long long ptr)
@ stdcall ScaleWindowExtEx(long long long long long ptr)
@ stdcall SelectBrushLocal(ptr ptr)
@ stdcall SelectClipPath(long long)
@ stdcall SelectClipRgn(long long)
@ stdcall SelectFontLocal(ptr ptr)
@ stdcall SelectObject(long long)
@ stdcall SelectPalette(long long long)
@ stdcall SetAbortProc(long ptr)
@ stdcall SetArcDirection(long long)
@ stdcall SetBitmapAttributes(ptr long)
@ stdcall SetBitmapBits(long long ptr) 
@ stdcall SetBitmapDimensionEx(long long long ptr) 
@ stdcall SetBkColor(long long)
@ stdcall SetBkMode(long long)
@ stdcall SetBoundsRect(long ptr long)
@ stdcall SetBrushAttributes(ptr long)
@ stdcall SetBrushOrgEx(long long long ptr)
@ stdcall SetColorAdjustment(long ptr)
@ stdcall SetColorSpace(long long)
@ stdcall SetDCBrushColor(long long)
@ stdcall SetDCPenColor(long long)
@ stdcall SetDIBColorTable(long long long ptr)
@ stdcall SetDIBits(long long long long ptr ptr long)
@ stdcall SetDIBitsToDevice(long long long long long long long long long ptr ptr long)
@ stdcall SetDeviceGammaRamp(long ptr)
@ stdcall SetEnhMetaFileBits(long ptr)
@ stdcall SetFontEnumeration(ptr) 
@ stdcall SetGraphicsMode(long long)
@ stdcall SetICMMode(long long)
@ stdcall SetICMProfileA(long str)
@ stdcall SetICMProfileW(long wstr)
@ stdcall SetLayout(long long)
@ stdcall SetLayoutWidth(ptr long long)
@ stdcall SetMagicColors(ptr long long) 
@ stdcall SetMapMode(long long)
@ stdcall SetMapperFlags(long long)
@ stdcall SetMetaFileBitsEx(long ptr)
@ stdcall SetMetaRgn(long)
@ stdcall SetMiterLimit(long long ptr)
@ stdcall SetPaletteEntries(long long long ptr)
@ stdcall SetPixel(long long long long)
@ stdcall SetPixelFormat(long long ptr)
@ stdcall SetPixelV(long long long long)
@ stdcall SetPolyFillMode(long long)
@ stdcall SetROP2(long long)
@ stdcall SetRectRgn(long long long long long)
@ stdcall SetRelAbs(long long)
@ stdcall SetStretchBltMode(long long)
@ stdcall SetSystemPaletteUse(long long) 
@ stdcall SetTextAlign(long long)
@ stdcall SetTextCharacterExtra(long long)
@ stdcall SetTextColor(long long)
@ stdcall SetTextJustification(long long long)
@ stdcall SetViewportExtEx(long long long ptr)
@ stdcall SetViewportOrgEx(long long long ptr)
@ stdcall SetVirtualResolution(long long long long long) 
@ stdcall SetWinMetaFileBits(long ptr long ptr)
@ stdcall SetWindowExtEx(long long long ptr)
@ stdcall SetWindowOrgEx(long long long ptr)
@ stdcall SetWorldTransform(long ptr)
@ stdcall StartDocA(long ptr)
@ stdcall StartDocW(long ptr)
@ stdcall StartFormPage(ptr)
@ stdcall StartPage(long)
@ stdcall StretchBlt(long long long long long long long long long long long)
@ stdcall StretchDIBits(long long long long long long long long long ptr ptr long long)
@ stdcall StrokeAndFillPath(long)
@ stdcall StrokePath(long)
@ stdcall SwapBuffers(long)
@ stdcall TextOutA(long long long str long)
@ stdcall TextOutW(long long long wstr long)
@ stdcall TranslateCharsetInfo(ptr ptr long)
@ stdcall UnloadNetworkFonts(long)
@ stdcall UnrealizeObject(long)
@ stdcall UpdateColors(long)
@ stdcall UpdateICMRegKeyA(long str str long)
@ stdcall UpdateICMRegKeyW(long wstr wstr long)
@ stdcall WidenPath(long)
@ stdcall XFORMOBJ_bApplyXform(ptr long long ptr ptr) 
@ stdcall XFORMOBJ_iGetXform(ptr ptr) 
@ stdcall XLATEOBJ_cGetPalette(ptr long long ptr)
@ stdcall XLATEOBJ_hGetColorTransform(ptr)
@ stdcall XLATEOBJ_iXlate(ptr long) 
@ stdcall XLATEOBJ_piVector(ptr)
@ stdcall bInitSystemAndFontsDirectoriesW(wstr wstr)
@ stdcall bMakePathNameW(wstr wstr wstr long)
@ stdcall cGetTTFFromFOT(long long long long long long long)
@ stdcall gdiPlaySpoolStream(long long long long long long)

#Vista functions
@ stdcall D3DKMTCheckMonitorPowerState(ptr)
@ stdcall D3DKMTCheckVidPnExclusiveOwnership(ptr)
#@ stdcall D3DKMTCloseAdapter(ptr)
@ stdcall D3DKMTCreateDCFromMemory(ptr)
#@ stdcall D3DKMTCreateDevice(ptr)
@ stdcall D3DKMTDestroyDCFromMemory(ptr)
#@ stdcall D3DKMTDestroyDevice(ptr)
#@ stdcall D3DKMTEscape(ptr)
#@ stdcall D3DKMTOpenAdapterFromGdiDisplayName(ptr)
@ stdcall D3DKMTOpenAdapterFromHdc(ptr)
@ stdcall D3DKMTOpenAdapterFromLuid(ptr)
@ stdcall D3DKMTQueryStatistics(ptr)
@ stdcall D3DKMTQueryVideoMemoryInfo(ptr)
@ stdcall D3DKMTSetQueuedLimit(ptr)
#@ stdcall D3DKMTSetVidPnSourceOwner(ptr)
@ stdcall GetFontFileData(long long int64 ptr long)
@ stub LoadImageColorMatcherA
@ stub LoadImageColorMatcherW 

#Fowarded to d3dkmt ()
@ stdcall D3DKMTAcquireKeyedMutex(ptr) d3dkmt.D3DKMTAcquireKeyedMutex
@ stdcall D3DKMTCloseAdapter(ptr) d3dkmt.D3DKMTCloseAdapter
@ stdcall D3DKMTConfigureSharedResource(ptr) d3dkmt.D3DKMTConfigureSharedResource
@ stdcall D3DKMTCreateAllocation(ptr) d3dkmt.D3DKMTCreateAllocation
@ stdcall D3DKMTCreateAllocation2(ptr) d3dkmt.D3DKMTCreateAllocation2
@ stdcall D3DKMTCreateContext(ptr) d3dkmt.D3DKMTCreateContext
@ stdcall D3DKMTCreateDevice(ptr) d3dkmt.D3DKMTCreateDevice
@ stdcall D3DKMTCreateSynchronizationObject(ptr) d3dkmt.D3DKMTCreateSynchronizationObject
@ stdcall D3DKMTCreateSynchronizationObject2(ptr) d3dkmt.D3DKMTCreateSynchronizationObject2
@ stdcall D3DKMTDestroyAllocation(ptr) d3dkmt.D3DKMTDestroyAllocation
@ stdcall D3DKMTDestroyContext(ptr) d3dkmt.D3DKMTDestroyContext
@ stdcall D3DKMTDestroyDevice(ptr) d3dkmt.D3DKMTDestroyDevice
@ stdcall D3DKMTDestroyKeyedMutex(ptr) d3dkmt.D3DKMTDestroyKeyedMutex
@ stdcall D3DKMTDestroySynchronizationObject(ptr) d3dkmt.D3DKMTDestroySynchronizationObject
@ stdcall D3DKMTEscape(ptr) d3dkmt.D3DKMTEscape
@ stdcall D3DKMTGetContextSchedulingPriority(ptr) d3dkmt.D3DKMTGetContextSchedulingPriority
@ stdcall D3DKMTGetDeviceSchedulingPriority(ptr) d3dkmt.D3DKMTGetDeviceSchedulingPriority
@ stdcall D3DKMTGetDeviceState(ptr) d3dkmt.D3DKMTGetDeviceState
@ stdcall D3DKMTGetDisplayModeList(ptr) d3dkmt.D3DKMTGetDisplayModeList
@ stdcall D3DKMTGetMultisampleMethodList(ptr) d3dkmt.D3DKMTGetMultisampleMethodList
@ stdcall D3DKMTGetRuntimeData(ptr) d3dkmt.D3DKMTGetRuntimeData
@ stdcall D3DKMTGetSharedPrimaryHandle(ptr) d3dkmt.D3DKMTGetSharedPrimaryHandle
@ stdcall D3DKMTGetThunkVersion(ptr) d3dkmt.D3DKMTGetThunkVersion
@ stdcall D3DKMTLock(ptr) d3dkmt.D3DKMTLock
@ stdcall D3DKMTOpenAdapterFromDeviceName(ptr) d3dkmt.D3DKMTOpenAdapterFromDeviceName
@ stdcall D3DKMTOpenAdapterFromGdiDisplayName(ptr) d3dkmt.D3DKMTOpenAdapterFromGdiDisplayName
@ stdcall D3DKMTOpenKeyedMutex(ptr) d3dkmt.D3DKMTOpenKeyedMutex
@ stdcall D3DKMTOpenResource(ptr) d3dkmt.D3DKMTOpenResource
@ stdcall D3DKMTOpenResource2(ptr) d3dkmt.D3DKMTOpenResource2
@ stdcall D3DKMTOpenSynchronizationObject(ptr) d3dkmt.D3DKMTOpenSynchronizationObject
@ stdcall D3DKMTPresent(ptr) d3dkmt.D3DKMTPresent
@ stdcall D3DKMTQueryAdapterInfo(ptr) d3dkmt.D3DKMTQueryAdapterInfo
@ stdcall D3DKMTQueryAllocationResidency(ptr) d3dkmt.D3DKMTQueryAllocationResidency
@ stdcall D3DKMTQueryResourceInfo(ptr) d3dkmt.D3DKMTQueryResourceInfo
@ stdcall D3DKMTReleaseKeyedMutex(ptr) d3dkmt.D3DKMTReleaseKeyedMutex
@ stdcall D3DKMTRender(ptr) d3dkmt.D3DKMTRender
@ stdcall D3DKMTSetAllocationPriority(ptr) d3dkmt.D3DKMTSetAllocationPriority
@ stdcall D3DKMTSetContextSchedulingPriority(ptr) d3dkmt.D3DKMTSetContextSchedulingPriority
@ stdcall D3DKMTSetDeviceSchedulingPriority(ptr) d3dkmt.D3DKMTSetDeviceSchedulingPriority
@ stdcall D3DKMTSetDisplayMode(ptr) d3dkmt.D3DKMTSetDisplayMode
@ stdcall D3DKMTSetDisplayPrivateDriverFormat(ptr) d3dkmt.D3DKMTSetDisplayPrivateDriverFormat
@ stdcall D3DKMTSetGammaRamp(ptr) d3dkmt.D3DKMTSetGammaRamp
@ stdcall D3DKMTSetVidPnSourceOwner(ptr) d3dkmt.D3DKMTSetVidPnSourceOwner
@ stdcall D3DKMTSignalSynchronizationObject(ptr) d3dkmt.D3DKMTSignalSynchronizationObject
@ stdcall D3DKMTSignalSynchronizationObject2(ptr) d3dkmt.D3DKMTSignalSynchronizationObject2
@ stdcall D3DKMTUnlock(ptr) d3dkmt.D3DKMTUnlock
@ stdcall D3DKMTWaitForSynchronizationObject(ptr) d3dkmt.D3DKMTWaitForSynchronizationObject
@ stdcall D3DKMTWaitForSynchronizationObject2(ptr) d3dkmt.D3DKMTWaitForSynchronizationObject2
@ stdcall D3DKMTWaitForVerticalBlankEvent(ptr) d3dkmt.D3DKMTWaitForVerticalBlankEvent

#Win7 functions
@ stdcall GetFontFileInfo(long long ptr long long)
@ stdcall GetFontRealizationInfo(long ptr)
@ stdcall GdiGetBitmapBitsSize(ptr) #please, be careful with this function!