package proto.mail.mail501 {
	import com.netease.protobuf.*;
	import flash.utils.IExternalizable;
	import flash.utils.IDataOutput;
	import flash.utils.IDataInput;
	import flash.errors.IOError;
	import proto.mail.mail501.MailInfo;
	// @@protoc_insertion_point(imports)
	// @@protoc_insertion_point(class_metadata)
	public final class dataPacket extends Message implements IExternalizable {
		private var curPage_:int;
		private var hasCurPage_:Boolean = false;
		public function get hasCurPage():Boolean {
			return hasCurPage_;
		}
		public function set curPage(value:int):void {
			hasCurPage_ = true;
			curPage_ = value;
		}
		public function get curPage():int {
			return curPage_;
		}
		private var maxPage_:int;
		private var hasMaxPage_:Boolean = false;
		public function get hasMaxPage():Boolean {
			return hasMaxPage_;
		}
		public function set maxPage(value:int):void {
			hasMaxPage_ = true;
			maxPage_ = value;
		}
		public function get maxPage():int {
			return maxPage_;
		}
		private var responseMailType_:int;
		private var hasResponseMailType_:Boolean = false;
		public function get hasResponseMailType():Boolean {
			return hasResponseMailType_;
		}
		public function set responseMailType(value:int):void {
			hasResponseMailType_ = true;
			responseMailType_ = value;
		}
		public function get responseMailType():int {
			return responseMailType_;
		}
		[ArrayElementType("proto.mail.mail501.MailInfo")]
		public var mailinfo:Array = [];
		public function writeExternal(output:IDataOutput):void {
			if (hasCurPage) {
				WriteUtils.writeTag(output, WireType.VARINT, 1);
				WriteUtils.write_TYPE_INT32(output, curPage);
			}
			if (hasMaxPage) {
				WriteUtils.writeTag(output, WireType.VARINT, 2);
				WriteUtils.write_TYPE_INT32(output, maxPage);
			}
			if (hasResponseMailType) {
				WriteUtils.writeTag(output, WireType.VARINT, 3);
				WriteUtils.write_TYPE_INT32(output, responseMailType);
			}
			for (var mailinfoIndex:uint = 0; mailinfoIndex < mailinfo.length; ++mailinfoIndex) {
				WriteUtils.writeTag(output, WireType.LENGTH_DELIMITED, 4);
				WriteUtils.write_TYPE_MESSAGE(output, mailinfo[mailinfoIndex]);
			}
		}
		public function readExternal(input:IDataInput):void {
			var curPageCount:uint = 0;
			var maxPageCount:uint = 0;
			var responseMailTypeCount:uint = 0;
			while (input.bytesAvailable != 0) {
				var tag:Tag = ReadUtils.readTag(input);
				switch (tag.number) {
				case 1:
					if (curPageCount != 0) {
						throw new IOError('Bad data format.');
					}
					++curPageCount;
					curPage = ReadUtils.read_TYPE_INT32(input);
					break;
				case 2:
					if (maxPageCount != 0) {
						throw new IOError('Bad data format.');
					}
					++maxPageCount;
					maxPage = ReadUtils.read_TYPE_INT32(input);
					break;
				case 3:
					if (responseMailTypeCount != 0) {
						throw new IOError('Bad data format.');
					}
					++responseMailTypeCount;
					responseMailType = ReadUtils.read_TYPE_INT32(input);
					break;
				case 4:
					mailinfo.push(ReadUtils.read_TYPE_MESSAGE(input, new proto.mail.mail501.MailInfo));
					break;
				default:
					ReadUtils.skip(input, tag.wireType);
				}
			}
		}
	}
}
