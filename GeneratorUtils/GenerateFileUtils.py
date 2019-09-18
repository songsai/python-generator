# coding=utf-8
import os, codecs


class GenerateFileUtils:
    def firstLower(self, string):
        return string[:1].lower() + string[1:]

    def beanFileWriter(self, className, classComment, fileds, filedComments, isNeeds, type):
        if type == 1:
            className = className + "Request"
            url = 'C:\\Users\\11941\\Desktop\\python\\请求消息体\\' + className + ".java"
            package = "request"
            baseClass = "BaseRequest"
        else:
            className = className + "Response"
            url = 'C:\\Users\\11941\\Desktop\\python\\返回消息体\\' + className + ".java"
            package = "response"
            baseClass = "BaseResponse"

        if os.path.exists(url):
            print("-------已经存在该文件，无需重复生成--------")
            return
        else:
            savingtxtmsg = codecs.open(url, 'a', 'utf-8')
            savingtxtmsg.write("package ng.serviceplatform.entity." + package + ".pa;\n\n")
            savingtxtmsg.write('/**\n')
            savingtxtmsg.write('* \n')
            savingtxtmsg.write('* ' + classComment + '\n')
            savingtxtmsg.write('* \n')
            savingtxtmsg.write('* @author Songsai\n')
            savingtxtmsg.write('* @date 2019/9/5\n')
            savingtxtmsg.write('* \n')
            savingtxtmsg.write('*/\n')
            savingtxtmsg.write('public class ' + className + ' extends ' + baseClass + ' {\n\n')
            # 开始写入成员变量
            for i in range(len(fileds)):
                savingtxtmsg.write('    /**\n')
                savingtxtmsg.write('    * ' + filedComments[i] + '\n')
                savingtxtmsg.write('    */\n')
                savingtxtmsg.write(
                    '    @ApiModelProperty(value="' + filedComments[i] + '", name="' + fileds[i] + '")\n')
                if isNeeds[i] == 'Y':
                    savingtxtmsg.write('    @NotBlank(message="' + filedComments[i] + '不能为空")\n')
                savingtxtmsg.write('    private String ' + fileds[i] + ';\n\n')

            savingtxtmsg.write('}\n')
            savingtxtmsg.close()

    def atomicFileWriter(self, className, classComment):
        url = 'C:\\Users\\11941\\Desktop\\python\\atomic\\' + className + ".java"
        response = className + 'Response'
        blankSpace = '    '
        blankSpace2 = '        '
        if os.path.exists(url):
            print("-------已经存在该文件，无需重复生成--------")
            return
        else:
            savingtxtmsg = codecs.open(url, 'a', 'utf-8')
            savingtxtmsg.write("package ng.serviceplatform.atomic.pa;\n\n")
            savingtxtmsg.write('import java.util.Map;\n\n')
            savingtxtmsg.write('/**\n')
            savingtxtmsg.write('* \n')
            savingtxtmsg.write('* ' + classComment + '\n')
            savingtxtmsg.write('* \n')
            savingtxtmsg.write('* @author Songsai\n')
            savingtxtmsg.write('* @date 2019/9/6\n')
            savingtxtmsg.write('* \n')
            savingtxtmsg.write('*/\n')
            savingtxtmsg.write('@Component\n')
            savingtxtmsg.write('public class ' + className + ' {\n\n')
            savingtxtmsg.write(blankSpace + 'public ' + response + ' request(' + className + 'Request req){\n\n')
            # 开始写入方法内容
            savingtxtmsg.write(blankSpace2 + 'String reqs = BeanMapUtils.beanToMap(req);\n')
            savingtxtmsg.write(blankSpace2 + 'Map<String,Object> returnMap = null;\n')
            savingtxtmsg.write(blankSpace2 + 'try {\n')
            savingtxtmsg.write(
                blankSpace2 + '    returnMap = PABankSDK.getInstance().apiInter(reqs,"' + className + '");\n')
            savingtxtmsg.write(blankSpace2 + '} catch (Exception e) {\n')
            savingtxtmsg.write(blankSpace2 + '    throw new ServiceException("500","调用平安银行接口失败");\n')
            savingtxtmsg.write(blankSpace2 + '}\n')
            savingtxtmsg.write(blankSpace2 + '// 处理返回消息体\n')
            savingtxtmsg.write(
                blankSpace2 + response + ' response = (' + response + ') JsonToBean.getJson(' + response + '.class, returnMap);\n')
            savingtxtmsg.write(blankSpace2 + 'return response;\n')
            savingtxtmsg.write(blankSpace + '}\n')
            savingtxtmsg.write('}\n')
            savingtxtmsg.close()

    def controllerFileWriter(self, className, classComment):
        menthodName = self.firstLower(className)
        response = className + 'Response'
        request = className + 'Request'

        url = 'C:\\Users\\11941\\Desktop\\python\\controller\\controller.java'
        blankSpace = '    '
        savingtxtmsg = codecs.open(url, 'a', 'utf-8')
        # savingtxtmsg.write('@ApiOperation(value = "' + classComment + '", notes = "' + classComment + '")\n')
        # savingtxtmsg.write('@RequestMapping(value="/'+menthodName+'", method=RequestMethod.POST)\n')
        # savingtxtmsg.write('public '+response+' '+ menthodName+'(@RequestBody @Valid '+request+' req){\n')
        # # 开始写入方法内容
        # savingtxtmsg.write(blankSpace + response+' response = '+menthodName+'.request(req);\n')
        # savingtxtmsg.write(blankSpace+ 'return response;\n')
        # savingtxtmsg.write('}\n')
        # savingtxtmsg.close()
        savingtxtmsg.write('@Autowired\n')
        savingtxtmsg.write(className + ' ' + menthodName + ';\n\n')
